from ds.visual.marimekko.MarimekkoAxisMixin import MarimekkoAxisMixin
from ds.visual.marimekko.MarimekkoGeometryMixin import MarimekkoGeometryMixin
from ds.visual.marimekko.MarimekkoHoverMixin import MarimekkoHoverMixin
from ds.visual.marimekko.MarimekkoPlotMixin import MarimekkoPlotMixin
from ds.visual.StackedBarChart import StackedBarChart


class MarimekkoChart(
    MarimekkoAxisMixin,
    MarimekkoPlotMixin,
    MarimekkoHoverMixin,
    MarimekkoGeometryMixin,
    StackedBarChart,
):

    def _build_title(self):
        return (
            f"{self.y_cell_key} by {self.x_dim_key}"
            f", marimekko by {self.stack_dim_key}"
        )

    def _get_title_text(self):
        return (
            f"{self._get_entity_name()} {self.y_cell_key} by "
            f"{self.x_dim_key}, marimekko by {self.stack_dim_key}"
        )

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        self._init_hover()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset)
        self._add_color_legend(fig, self.stack_color_idx, self.stack_dim_key)
        self._connect_hover(fig)
        self._hide_empty_axes(axes, n_datumsets)
