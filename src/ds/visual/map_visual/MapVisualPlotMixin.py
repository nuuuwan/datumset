import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.ticker import FuncFormatter


class MapVisualPlotMixin:

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, ctx):
        gdf = self._get_colored_gdf(sub_datumset, ctx)
        gdf.plot(
            color=list(gdf["color"]),
            ax=sub_ax,
            edgecolor=self.REGION_EDGE_COLOR,
            linewidth=self.REGION_EDGE_LINEWIDTH,
        )
        self._add_region_labels(gdf, sub_ax, fig)
        sub_ax.set_axis_off()
        self._set_square_subfigure_title(sub_ax, sub_datumset)

    def _add_map_legend(self, fig, ctx):
        if ctx["mode"] == "category":
            self._add_color_legend(
                fig, ctx["color_idx"], self.region_color_dim_key
            )
            return
        self._add_colorbar(fig, ctx["vmin"], ctx["vmax"], ctx["cmap"])

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
        ctx = self._get_color_context()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(fig, sub_ax, sub_datumset, ctx)
        self._add_map_legend(fig, ctx)
        self._hide_empty_axes(axes, n_datumsets)
