import math

from matplotlib.patches import Rectangle
from shapely.geometry import Polygon

from ds.visual.square_map.SquareTextFit import SquareTextFit


class SquareShapeMixin:

    @staticmethod
    def _shape_centers(bounds, radius):
        minx, miny, maxx, maxy = bounds
        side = 2 * radius
        centers = []
        y = miny
        while y <= maxy + side:
            x = minx
            while x <= maxx + side:
                centers.append((x, y))
                x += side
            y += side
        return centers

    def _initial_radius(self, bounds, target):
        minx, miny, maxx, maxy = bounds
        area = max((maxx - minx) * (maxy - miny), 1e-12)
        return math.sqrt(area / max(target, 1)) / 2

    def _draw_shape(self, ax, x, y, radius, color):
        ax.add_patch(
            Rectangle(
                (x - radius, y - radius),
                2 * radius,
                2 * radius,
                facecolor=color,
                edgecolor=self.SHAPE_EDGE_COLOR,
                linewidth=self.SHAPE_EDGE_WIDTH,
            )
        )

    @staticmethod
    def _shape_polygon(x, y, radius):
        return Polygon(
            [
                (x - radius, y - radius),
                (x + radius, y - radius),
                (x + radius, y + radius),
                (x - radius, y + radius),
            ]
        )

    def _best_label_fit(self, points, radius):
        return SquareTextFit.best_label_fit(points, radius)
