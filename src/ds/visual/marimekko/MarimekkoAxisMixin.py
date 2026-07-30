from matplotlib.ticker import FuncFormatter
from utils_future import Percent


class MarimekkoAxisMixin:

    def _get_bar_centers(self, geometries):
        return [left + width / 2.0 for left, width in geometries]

    def _set_marimekko_yaxis(self, sub_ax):
        sub_ax.set_ylabel("Share")
        sub_ax.set_ylim(0, self.BAR_HEIGHT)
        sub_ax.yaxis.set_major_formatter(
            FuncFormatter(lambda value, _: Percent(value).humanize)
        )

    def _set_marimekko_xaxis(
        self, sub_ax, geometries, x_labels, sub_datumset
    ):
        centers = self._get_bar_centers(geometries)
        axis_width_px = self._get_axis_width_px(sub_ax)
        display_labels = [
            self._shorten_x_label(sub_ax, x_label, width * axis_width_px)
            for (_, width), x_label in zip(geometries, x_labels)
        ]
        label_colors = self._get_x_label_colors(sub_datumset, x_labels)
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

    def _style_marimekko_subfigure(
        self,
        sub_ax,
        geometries,
        x_labels,
        totals,
        sub_datumset,
    ):
        sub_ax.set_xlim(0, 1)
        sub_ax.set_box_aspect(self._get_box_aspect())
        self._set_marimekko_yaxis(sub_ax)
        self._set_marimekko_xaxis(sub_ax, geometries, x_labels, sub_datumset)
        self._add_bar_total_labels(sub_ax, geometries, totals)
        self._set_subfigure_title(sub_ax, sub_datumset)
