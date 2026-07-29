from matplotlib.ticker import FuncFormatter


class MarimekkoAxisMixin:

    def _format_share(self, value, _pos):
        return "%.0f%%" % (value * 100.0 / self.BAR_HEIGHT)

    def _get_bar_centers(self, geometries):
        return [left + width / 2.0 for left, width in geometries]

    def _set_marimekko_yaxis(self, sub_ax):
        sub_ax.set_ylabel("Share")
        sub_ax.set_ylim(0, self.BAR_HEIGHT)
        sub_ax.yaxis.set_major_formatter(FuncFormatter(self._format_share))

    def _set_marimekko_xaxis(self, sub_ax, geometries, x_labels):
        centers = self._get_bar_centers(geometries)
        display_labels = [
            self._format_visual_value(x_label) for x_label in x_labels
        ]
        sub_ax.set_xticks(centers)
        sub_ax.set_xticklabels(
            display_labels,
            fontsize=6,
            rotation=90,
            ha="center",
            va="top",
        )
        sub_ax.tick_params(axis="x", pad=1)

    def _add_bar_total_labels(self, sub_ax, geometries, totals):
        offset = self.BAR_HEIGHT * 0.015
        for (left, width), total in zip(geometries, totals):
            if width <= 0 or total <= 0:
                continue
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
        self._set_marimekko_yaxis(sub_ax)
        self._set_marimekko_xaxis(sub_ax, geometries, x_labels)
        self._add_bar_total_labels(sub_ax, geometries, totals)
        sub_ax.set_box_aspect(1)
        self._set_subfigure_title(sub_ax, sub_datumset)
