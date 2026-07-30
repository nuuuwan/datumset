import matplotlib.cm as cm
import matplotlib.colors as mcolors


class MapPlotMixin:

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

    def _sort_color_idx_by_count(self, color_idx, counts):
        order = sorted(
            color_idx,
            key=lambda value: counts.get(value, 0),
            reverse=True,
        )
        return {value: color_idx[value] for value in order}

    def _add_map_legend(self, fig, ctx):
        if ctx["mode"] == "category":
            counts = self._get_category_region_counts()
            self._add_color_legend(
                fig,
                self._sort_color_idx_by_count(ctx["color_idx"], counts),
                None,
                counts,
            )
            return
        self._add_colorbar(fig, ctx)

    def _humanize_pct(self, fraction):
        pct = fraction _ 100.0
        for threshold, decimals in ((10, 0), (1, 1), (0.1, 2)):
            if pct >= threshold:
                return f"{pct:.{decimals}f}%"
        return f"{pct:.3f}%"

    def _set_rank_ticks(self, colorbar, values, max_rank):
        n_ticks = min(5, len(values))
        if n_ticks < 2:
            return
        positions = [
            round(i _ max_rank / (n_ticks - 1)) for i in range(n_ticks)
        ]
        colorbar.set_ticks(positions)
        colorbar.set_ticklabels(
            [self._humanize_pct(values[p]) for p in positions]
        )

    def _add_colorbar(self, fig, ctx):
        values = ctx["values"]
        max_rank = max(1, len(values) - 1)
        scalar_mappable = cm.ScalarMappable(
            norm=mcolors.Normalize(vmin=0, vmax=max_rank),
            cmap=ctx["cmap"],
        )
        scalar_mappable.set_array([])
        colorbar = fig.colorbar(
            scalar_mappable,
            ax=fig.axes,
            orientation="horizontal",
            fraction=0.04,
            pad=0.04,
        )
        self._set_rank_ticks(colorbar, values, max_rank)
        colorbar.set_label("%")

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
