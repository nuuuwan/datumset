from matplotlib.patches import RegularPolygon


class HexMapDrawMixin:

    HEX_EDGE_COLOR = "#ffffff"
    HEX_EDGE_WIDTH = 0.3

    def _get_region_centroids(self, gdf):
        return {
            row["region_id"]: (
                row.geometry.centroid.x,
                row.geometry.centroid.y,
            )
            for _, row in gdf.iterrows()
        }

    def _get_hex_layout(self, gdf):
        centroids = self._get_region_centroids(gdf)
        weights = self._get_region_id_to_weight(gdf)
        counts = self.get_counts(weights)
        centers, radius = self.build_grid(
            tuple(gdf.total_bounds), sum(counts.values())
        )
        return radius, self.assign(centroids, counts, centers)

    def _draw_hex(self, ax, x, y, radius, color):
        ax.add_patch(
            RegularPolygon(
                (x, y),
                numVertices=6,
                radius=radius,
                orientation=0,
                facecolor=color,
                edgecolor=self.HEX_EDGE_COLOR,
                linewidth=self.HEX_EDGE_WIDTH,
            )
        )

    def _set_hex_limits(self, ax, radius, hexes):
        xs = [x for _, x, _ in hexes]
        ys = [y for _, _, y in hexes]
        if not xs:
            return
        ax.set_xlim(min(xs) - radius, max(xs) + radius)
        ax.set_ylim(min(ys) - radius, max(ys) + radius)
        ax.set_aspect("equal")

    def _draw_hexes(self, ax, radius, hexes, region_color):
        for region_id, x, y in hexes:
            color = region_color.get(region_id, "#cccccc")
            self._draw_hex(ax, x, y, radius, color)
        self._set_hex_limits(ax, radius, hexes)

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, ctx):
        gdf = self._get_colored_gdf(sub_datumset, ctx)
        region_color = dict(zip(gdf["region_id"], gdf["color"]))
        radius, hexes = self._get_hex_layout(gdf)
        self._draw_hexes(sub_ax, radius, hexes, region_color)
        self._draw_boundaries(sub_ax, radius, hexes)
        self._add_hex_labels(fig, sub_ax, radius, hexes, gdf)
        sub_ax.set_axis_off()
        self._set_square_subfigure_title(sub_ax, sub_datumset)
