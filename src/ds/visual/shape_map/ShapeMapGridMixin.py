class ShapeMapGridMixin:

    GRID_FACTOR = 1.3
    MAX_GRID_ITERATIONS = 12

    def build_grid(self, bounds, total_count):
        target = max(total_count * self.GRID_FACTOR, total_count + 1)
        radius = self._initial_radius(bounds, target)
        centers = self._shape_centers(bounds, radius)
        for _ in range(self.MAX_GRID_ITERATIONS):
            if len(centers) >= total_count:
                break
            radius *= 0.85
            centers = self._shape_centers(bounds, radius)
        return centers, radius
