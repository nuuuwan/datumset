from scipy.optimize import linear_sum_assignment


class ShapeMapAssignMixin:

    @staticmethod
    def _build_slots(region_to_centroid, counts):
        slots = []
        for region_id, count in counts.items():
            centroid = region_to_centroid[region_id]
            for _ in range(count):
                slots.append((region_id, centroid))
        return slots

    @staticmethod
    def _cost_matrix(slots, centers):
        cost = []
        for _, (cx, cy) in slots:
            cost.append([(cx - x) ** 2 + (cy - y) ** 2 for (x, y) in centers])
        return cost

    def assign(self, region_to_centroid, counts, centers):
        slots = self._build_slots(region_to_centroid, counts)
        cost = self._cost_matrix(slots, centers)
        rows, cols = linear_sum_assignment(cost)
        shapes = []
        for i, j in zip(rows, cols):
            x, y = centers[j]
            shapes.append((slots[i][0], x, y))
        return shapes
