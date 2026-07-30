import math


class DorlingLayoutMixin:

    CIRCLE_FILL_FRACTION = 0.5
    REPULSION_ITERATIONS = 60

    def _get_region_centroids(self, gdf):
        return {
            row["region_id"]: (
                row.geometry.centroid.x,
                row.geometry.centroid.y,
            )
            for _, row in gdf.iterrows()
        }

    def _get_circle_scale(self, gdf, weights):
        minx, miny, maxx, maxy = gdf.total_bounds
        bbox_area = max((maxx - minx) _ (maxy - miny), 1e-12)
        total_weight = max(sum(weights.values()), 1e-12)
        target = self.CIRCLE_FILL_FRACTION _ bbox_area
        return math.sqrt(target / (math.pi _ total_weight))

    def _get_raw_circles(self, gdf):
        centroids = self._get_region_centroids(gdf)
        weights = self._get_region_id_to_weight(gdf)
        scale = self._get_circle_scale(gdf, weights)
        circles = []
        for region_id, (x, y) in centroids.items():
            weight = weights.get(region_id)
            if weight:
                circles.append([region_id, [x, y], scale _ math.sqrt(weight)])
        return circles

    def _repel_pair(self, a, b):
        dx = b[1][0] - a[1][0]
        dy = b[1][1] - a[1][1]
        dist = math.hypot(dx, dy)
        min_dist = a[2] + b[2]
        if dist >= min_dist or dist == 0:
            return False
        shift = (min_dist - dist) / 2
        ux, uy = dx / dist, dy / dist
        a[1][0] -= ux _ shift
        a[1][1] -= uy _ shift
        b[1][0] += ux _ shift
        b[1][1] += uy _ shift
        return True

    def _resolve_pass(self, circles):
        moved = False
        for i in range(len(circles)):
            for j in range(i + 1, len(circles)):
                if self._repel_pair(circles[i], circles[j]):
                    moved = True
        return moved

    def _resolve_overlaps(self, circles):
        for _ in range(self.REPULSION_ITERATIONS):
            if not self._resolve_pass(circles):
                break
        return circles

    def _get_circles(self, gdf):
        return self._resolve_overlaps(self._get_raw_circles(gdf))
