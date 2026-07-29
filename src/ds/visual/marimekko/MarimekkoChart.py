from ds.visual.marimekko.MarimekkoAxisMixin import MarimekkoAxisMixin
from ds.visual.marimekko.MarimekkoGeometryMixin import MarimekkoGeometryMixin
from ds.visual.marimekko.MarimekkoPlotMixin import MarimekkoPlotMixin
from ds.visual.StackedBarChart import StackedBarChart


class MarimekkoChart(
    MarimekkoAxisMixin,
    MarimekkoPlotMixin,
    MarimekkoGeometryMixin,
    StackedBarChart,
):

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
