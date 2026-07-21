import numpy as np
from shapely.geometry import Point, Polygon


class LabelFitGeomMixin:

    @staticmethod
    def _largest_polygon(geom):
        if isinstance(geom, Polygon):
            return geom
        polys = [
            g for g in getattr(geom, 'geoms', []) if isinstance(g, Polygon)
        ]
        return max(polys, key=lambda g: g.area) if polys else geom

    @staticmethod
    def _interior_candidates(poly, n_cells=6):
        minx, miny, maxx, maxy = poly.bounds
        pts = []
        for i in range(n_cells):
            x = minx + (maxx - minx) * (i + 0.5) / n_cells
            for j in range(n_cells):
                y = miny + (maxy - miny) * (j + 0.5) / n_cells
                if poly.contains(Point(x, y)):
                    pts.append((x, y))
        if not pts:
            rp = poly.representative_point()
            return [(rp.x, rp.y)]
        return pts

    @staticmethod
    def _edges(poly):
        coords = np.array(poly.exterior.coords)
        ax, ay = coords[:-1, 0], coords[:-1, 1]
        bx, by = coords[1:, 0], coords[1:, 1]
        return ax, ay, bx - ax, by - ay
