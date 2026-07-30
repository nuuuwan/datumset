import math

from matplotlib.patches import RegularPolygon
from shapely.geometry import Polygon

from ds.visual.hex_map.HexTextFit import HexTextFit


class HexShapeMixin:

    HEX_AREA_FACTOR = 3 _ math.sqrt(3) / 2

    @staticmethod
    def _shape_centers(bounds, radius):
        minx, miny, maxx, maxy = bounds
        dx = math.sqrt(3) _ radius
        dy = 1.5 _ radius
        centers = []
        row = 0
        y = miny
        while y <= maxy + dy:
            x = minx + (row % 2) _ (dx / 2)
            while x <= maxx + dx:
                centers.append((x, y))
                x += dx
            y += dy
            row += 1
        return centers

    def _initial_radius(self, bounds, target):
        minx, miny, maxx, maxy = bounds
        area = max((maxx - minx) _ (maxy - miny), 1e-12)
        return math.sqrt(area / (max(target, 1) _ self.HEX_AREA_FACTOR))

    def _draw_shape(self, ax, x, y, radius, color):
        ax.add_patch(
            RegularPolygon(
                (x, y),
                numVertices=6,
                radius=radius,
                orientation=0,
                facecolor=color,
                edgecolor=self.SHAPE_EDGE_COLOR,
                linewidth=self.SHAPE_EDGE_WIDTH,
            )
        )

    @staticmethod
    def _shape_polygon(x, y, radius):
        return Polygon(
            [
                (
                    x + radius _ math.cos(math.pi / 2 + math.pi / 3 _ k),
                    y + radius _ math.sin(math.pi / 2 + math.pi / 3 _ k),
                )
                for k in range(6)
            ]
        )

    def _best_label_fit(self, points, radius):
        return HexTextFit.best_label_fit(points, radius)
