import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.ticker import FuncFormatter


class MapVisualPlotMixin:

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, vmin, vmax, cmap):
        gdf = self._get_gdf_with_values(sub_datumset)
        gdf.plot(
            column="value",
            ax=sub_ax,
            legend=False,
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            edgecolor=self.REGION_EDGE_COLOR,
            linewidth=self.REGION_EDGE_LINEWIDTH,
        )
        self._add_region_labels(gdf, sub_ax, fig, vmin, vmax, cmap)
        sub_ax.set_axis_off()
        self._set_square_subfigure_title(sub_ax, sub_datumset)

    def _add_colorbar(self, fig, vmin, vmax, cmap):
        scalar_mappable = cm.ScalarMappable(
            norm=mcolors.Normalize(vmin=vmin, vmax=vmax),
            cmap=cmap,
        )
        scalar_mappable.set_array([])
        colorbar = fig.colorbar(
            scalar_mappable,
            ax=fig.axes,
            orientation="horizontal",
            fraction=0.04,
            pad=0.04,
        )
        formatter = FuncFormatter(self._format_humanized_value)
        colorbar.formatter = formatter
        colorbar.ax.xaxis.set_major_formatter(formatter)
        colorbar.ax.xaxis.offsetText.set_visible(False)
        colorbar.update_ticks()
        colorbar.set_label(self.y_cell_key)

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        vmin, vmax = self._get_value_range()
        cmap = self._get_value_cmap()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(
                fig,
                sub_ax,
                sub_datumset,
                vmin,
                vmax,
                cmap,
            )
        self._add_colorbar(fig, vmin, vmax, cmap)
        self._hide_empty_axes(axes, n_datumsets)
