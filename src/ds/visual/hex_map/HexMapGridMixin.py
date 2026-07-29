import math


class HexMapGridMixin:

    GRID_FACTOR = 1.3
    MAX_GRID_ITERATIONS = 12
    HEX_AREA_FACTOR = 3 * math.sqrt(3) / 2

    @staticmethod
    def _hex_centers(bounds, radius):
        minx, miny, maxx, maxy = bounds
        dx = math.sqrt(3) * radius
        dy = 1.5 * radius
        centers = []
        row = 0
        y = miny
        while y <= maxy + dy:
            x = minx + (row % 2) * (dx / 2)
            while x <= maxx + dx:
                centers.append((x, y))
                x += dx
            y += dy
            row += 1
        return centers

    def _initial_radius(self, bounds, target):
        minx, miny, maxx, maxy = bounds
        area = max((maxx - minx) * (maxy - miny), 1e-12)
        return math.sqrt(area / (max(target, 1) * self.HEX_AREA_FACTOR))

    def build_grid(self, bounds, total_count):
        target = max(total_count * self.GRID_FACTOR, total_count + 1)
        radius = self._initial_radius(bounds, target)
        centers = self._hex_centers(bounds, radius)
        for _ in range(self.MAX_GRID_ITERATIONS):
            if len(centers) >= total_count:
                break
            radius *= 0.85
            centers = self._hex_centers(bounds, radius)
        return centers, radius
