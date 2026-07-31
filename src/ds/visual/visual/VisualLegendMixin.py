import math

import matplotlib.patches as mpatches


class VisualLegendMixin:

    LEGEND_FONTSIZE = 9
    LEGEND_TITLE_FONTSIZE = 10
    MAX_LEGEND_COLS = 4

    def _get_legend_ncol(self, n):
        if n <= self.MAX_LEGEND_COLS:
            return n
        n_rows = math.ceil(n / self.MAX_LEGEND_COLS)
        return math.ceil(n / n_rows)

    def _get_legend_label(self, value, value_counts):
        label = self._format_visual_value(value)
        if value_counts is None:
            return label
        count = value_counts.get(value, 0)
        if count == 0:
            return label
        return f"{label} ({count})"

    def _add_color_legend(
        self, fig, value_color_idx, title, value_counts=None
    ):
        legend_handles = [
            mpatches.Patch(
                color=color,
                label=self._get_legend_label(value, value_counts),
            )
            for value, color in value_color_idx.items()
        ]
        n = len(legend_handles)
        formatted_title = self._format_visual_value(title) if title else None
        fig.legend(
            handles=legend_handles,
            title=formatted_title,
            loc="lower center",
            bbox_to_anchor=(0.5, 0.01),
            ncol=self._get_legend_ncol(n),
            frameon=False,
            fontsize=self.LEGEND_FONTSIZE,
            title_fontsize=self.LEGEND_TITLE_FONTSIZE,
        )
