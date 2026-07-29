import math

from ds.visual.hex_map.HexMapGridMixin import HexMapGridMixin


class SquareMapGridMixin(HexMapGridMixin):

    @staticmethod
    def _hex_centers(bounds, radius):
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
