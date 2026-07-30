class ShapeMapDrawMixin:

    SHAPE_EDGE_COLOR = "#ffffff"
    SHAPE_EDGE_WIDTH = 0.2

    def _get_region_centroids(self, gdf):
        return {
            row["region_id"]: (
                row.geometry.centroid.x,
                row.geometry.centroid.y,
            )
            for _, row in gdf.iterrows()
        }

    def _get_shape_layout(self, gdf, sub_datumset):
        centroids = self._get_region_centroids(gdf)
        weights = self._get_region_id_to_weight(gdf, sub_datumset)
        counts = self.get_counts(weights, self._shared_value_per_shape)
        centers, radius = self.build_grid(
            tuple(gdf.total_bounds), sum(counts.values())
        )
        return radius, self.assign(centroids, counts, centers)

    def _set_shape_limits(self, ax, radius, shapes):
        xs = [x for _, x, _ in shapes]
        ys = [y for _, _, y in shapes]
        if not xs:
            return
        ax.set_xlim(min(xs) - radius, max(xs) + radius)
        ax.set_ylim(min(ys) - radius, max(ys) + radius)
        ax.set_aspect("equal")

    def _draw_shapes(self, ax, radius, shapes, region_color):
        for region_id, x, y in shapes:
            color = region_color.get(region_id, "#cccccc")
            self._draw_shape(ax, x, y, radius, color)
        self._set_shape_limits(ax, radius, shapes)

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, ctx):
        gdf = self._get_colored_gdf(sub_datumset, ctx)
        region_color = dict(zip(gdf["region_id"], gdf["color"]))
        radius, shapes = self._get_shape_layout(gdf, sub_datumset)
        self._draw_shapes(sub_ax, radius, shapes, region_color)
        self._draw_boundaries(sub_ax, radius, shapes)
        self._add_shape_labels(fig, sub_ax, radius, shapes, gdf)
        self._record_shape_values(gdf, shapes, sub_datumset)
        sub_ax.set_axis_off()
        self._set_square_subfigure_title(sub_ax, sub_datumset)
