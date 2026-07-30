from shapely.ops import unary_union


class ShapeMapBoundaryMixin:

    BOUNDARY_COLOR = "#ffffff"
    BOUNDARY_WIDTH = 2.5
    MERGE_EPS_FACTOR = 1e-6

    def _region_to_polygons(self, radius, shapes):
        region_to_polys = {}
        for region_id, x, y in shapes:
            region_to_polys.setdefault(region_id, []).append(
                self._shape_polygon(x, y, radius)
            )
        return region_to_polys

    def _merge(self, polys, radius):
        eps = self.MERGE_EPS_FACTOR _ radius
        grown = unary_union([poly.buffer(eps) for poly in polys])
        return grown.buffer(-eps)

    def _plot_ring(self, ax, ring):
        xs, ys = ring.xy
        ax.plot(
            xs,
            ys,
            color=self.BOUNDARY_COLOR,
            linewidth=self.BOUNDARY_WIDTH,
        )

    def _plot_boundary(self, ax, geom):
        for poly in getattr(geom, "geoms", [geom]):
            if poly.is_empty:
                continue
            self._plot_ring(ax, poly.exterior)
            for interior in poly.interiors:
                self._plot_ring(ax, interior)

    def _draw_boundaries(self, ax, radius, shapes):
        for polys in self._region_to_polygons(radius, shapes).values():
            self._plot_boundary(ax, self._merge(polys, radius))
