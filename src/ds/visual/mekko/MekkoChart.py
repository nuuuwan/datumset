from ds.visual.mekko.MekkoAxisMixin import MekkoAxisMixin
from ds.visual.mekko.MekkoGeometryMixin import MekkoGeometryMixin
from ds.visual.mekko.MekkoPlotMixin import MekkoPlotMixin
from ds.visual.stacked_bar_chart.StackedBarChart import StackedBarChart


class MekkoChart(
    MekkoAxisMixin,
    MekkoPlotMixin,
    MekkoGeometryMixin,
    StackedBarChart,
):

    def _excluded_dim_keys(self):
        return {self.x_dim_key, self.stack_dim_key}

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset)
        self._add_color_legend(
            fig,
            self.stack_color_idx,
            self.stack_dim_key,
            self._get_category_win_counts(),
        )
        self._hide_empty_axes(axes, n_datumsets)
