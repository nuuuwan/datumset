from matplotlib.ticker import FuncFormatter
from utils_future import Percent


class MekkoAxisMixin:

    def _get_bar_centers(self, geometries):
        return [left + width / 2.0 for left, width in geometries]

    def _set_mekko_yaxis(self, sub_ax):
        sub_ax.set_ylabel("Share")
        sub_ax.set_ylim(0, self.BAR_HEIGHT)
        sub_ax.yaxis.set_major_formatter(
            FuncFormatter(lambda value, _: Percent(value).humanize)
        )

    def _get_mekko_x_label(self, sub_ax, x_label, width):
        axis_width_px = self._get_axis_width_px(sub_ax)
        slot_px = width * axis_width_px
        formatted_label = self._format_mekko_x_label(x_label)
        if not self._can_shorten_dim(self.x_dim_key):
            max_chars = max(2, int(slot_px / self._get_px_per_char(sub_ax)))
            return self._wrap_x_label(formatted_label, max_chars)
        return self._shorten_formatted_x_label(
            sub_ax, formatted_label, slot_px
        )

    def _set_mekko_xaxis(self, sub_ax, geometries, x_labels, sub_datumset):
        centers = self._get_bar_centers(geometries)
        display_labels = [
            self._get_mekko_x_label(sub_ax, x_label, width)
            for (_, width), x_label in zip(geometries, x_labels)
        ]
        _, stack_labels, data = self._get_mekko_data(sub_datumset)
        label_colors = [
            self._get_x_label_color(x_label, stack_labels, data)
            for x_label in x_labels
        ]
        half_widths = [width / 2.0 * 0.9 for (_, width) in geometries]
        self._set_x_tick_labels(
            sub_ax,
            centers,
            display_labels,
            label_colors,
            half_widths,
        )

    def _add_bar_total_labels(self, sub_ax, geometries, totals):
        offset = self.BAR_HEIGHT * 0.015
        for (left, width), total in zip(geometries, totals):
            sub_ax.text(
                left + width / 2.0,
                self.BAR_HEIGHT + offset,
                self._format_humanized_value(float(total), None),
                ha="center",
                va="bottom",
                fontsize=7,
                color=self.SUBTITLE_COLOR,
            )

    def _style_mekko_subfigure(
        self,
        sub_ax,
        geometries,
        x_labels,
        totals,
        sub_datumset,
    ):
        sub_ax.set_xlim(0, 1)
        sub_ax.set_box_aspect(self._get_box_aspect())
        self._set_mekko_yaxis(sub_ax)
        self._set_mekko_xaxis(sub_ax, geometries, x_labels, sub_datumset)
        self._add_bar_total_labels(sub_ax, geometries, totals)
        self._set_subfigure_title(sub_ax, sub_datumset)
