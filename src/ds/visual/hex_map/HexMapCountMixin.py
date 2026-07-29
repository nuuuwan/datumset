class HexMapCountMixin:

    HEXMAP_ERROR = 0.1

    @staticmethod
    def _region_error(actual, ideal):
        return abs(actual - ideal) / ideal

    def _max_error(self, weights, value_per_hex):
        errors = []
        for weight in weights:
            ideal = weight / value_per_hex
            actual = max(1, round(ideal))
            errors.append(self._region_error(actual, ideal))
        return max(errors)

    def _candidates(self, weights):
        n_max = int(0.5 / self.HEXMAP_ERROR) + 2
        cap = min(weights) * (1 + self.HEXMAP_ERROR)
        values = {min(weights) * 2 * self.HEXMAP_ERROR}
        for weight in weights:
            for n in range(1, n_max + 1):
                value = weight * (1 + self.HEXMAP_ERROR) / n
                if value <= cap:
                    values.add(value)
        return sorted(values, reverse=True)

    def _value_per_hex(self, region_to_weight):
        weights = [w for w in region_to_weight.values() if w > 0]
        if not weights:
            return None
        tolerance = self.HEXMAP_ERROR + 1e-9
        for value in self._candidates(weights):
            if self._max_error(weights, value) <= tolerance:
                return value
        return min(weights) * 2 * self.HEXMAP_ERROR

    def get_counts(self, region_to_weight):
        value_per_hex = self._value_per_hex(region_to_weight)
        if value_per_hex is None:
            return {region_id: 1 for region_id in region_to_weight}
        return {
            region_id: max(1, round(weight / value_per_hex))
            for region_id, weight in region_to_weight.items()
        }
