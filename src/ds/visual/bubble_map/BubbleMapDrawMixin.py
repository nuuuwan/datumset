import math

from matplotlib.patches import Circle


class BubbleMapDrawMixin:

    BUBBLE_EDGE_COLOR = "#ffffff"
    BUBBLE_EDGE_WIDTH = 0.5
    BUBBLE_ALPHA = 0.7

    def _get_region_centroids(self, gdf):
        return {
            row["region_id"]: (
                row.geometry.centroid.x,
                row.geometry.centroid.y,
            )
            for _, row in gdf.iterrows()
        }

    def _get_bubble_scale(self, gdf, weights):
        minx, miny, maxx, maxy = gdf.total_bounds
        bbox_area = max((maxx - minx) * (maxy - miny), 1e-12)
        total_weight = max(sum(weights.values()), 1e-12)
        target = self.BUBBLE_FILL_FRACTION * bbox_area
        return math.sqrt(target / (math.pi * total_weight))

    def _get_bubbles(self, gdf):
        centroids = self._get_region_centroids(gdf)
        weights = self._get_region_id_to_weight(gdf)
        scale = self._get_bubble_scale(gdf, weights)
        bubbles = []
        for region_id, (x, y) in centroids.items():
            weight = weights.get(region_id)
            if weight:
                bubbles.append([region_id, [x, y], scale * math.sqrt(weight)])
        return bubbles

    def _draw_bubble(self, ax, xy, radius, color):
        ax.add_patch(
            Circle(
                xy,
                radius,
                facecolor=color,
                edgecolor=self.BUBBLE_EDGE_COLOR,
                linewidth=self.BUBBLE_EDGE_WIDTH,
                alpha=self.BUBBLE_ALPHA,
            )
        )

    def _draw_bubbles(self, ax, bubbles, region_color):
        for region_id, (x, y), radius in bubbles:
            color = region_color.get(region_id, "#cccccc")
            self._draw_bubble(ax, (x, y), radius, color)

    def _plot_basemap(self, sub_ax, gdf):
        gdf.plot(
            color="#f7f7f7",
            ax=sub_ax,
            edgecolor=self.REGION_EDGE_COLOR,
            linewidth=self.REGION_EDGE_LINEWIDTH,
        )

    def _set_map_limits(self, sub_ax, gdf):
        minx, miny, maxx, maxy = gdf.total_bounds
        sub_ax.set_xlim(minx, maxx)
        sub_ax.set_ylim(miny, maxy)
        sub_ax.set_aspect("equal")
        sub_ax.set_axis_off()

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, ctx):
        gdf = self._get_colored_gdf(sub_datumset, ctx)
        region_color = dict(zip(gdf["region_id"], gdf["color"]))
        self._plot_basemap(sub_ax, gdf)
        bubbles = self._get_bubbles(gdf)
        self._draw_bubbles(sub_ax, bubbles, region_color)
        self._set_map_limits(sub_ax, gdf)
        self._add_region_labels(gdf, sub_ax, fig)
        self._set_square_subfigure_title(sub_ax, sub_datumset)
