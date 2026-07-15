class DatumSerializeMixin:
    def get_measurement_for_class_name(self, class_name):
        for measurement in self.measurement_idx.values():
            if type(measurement).__name__ == class_name:
                return measurement
        return None

    def _get_extra_values(self, class_names_required):
        return {
            k: v.to_json()
            for k, v in self.measurement_idx.items()
            if v.__class__.__name__ not in class_names_required
        }

    def _get_nested_value(self, class_names_required, i):
        if i != len(class_names_required) - 1:
            return {}
        return self._get_extra_values(class_names_required)

    def to_data_inner(self, idx, measurement_part):
        class_names_required = measurement_part.split('*')
        idx_temp = idx
        for i, class_name in enumerate(class_names_required):
            measurement = self.get_measurement_for_class_name(class_name)
            value = measurement.to_json()
            if value not in idx:
                idx_temp[value] = self._get_nested_value(
                    class_names_required, i
                )
            idx_temp = dict(
                sorted(idx_temp.items(), key=lambda item: item[0])
            )
            idx_temp = idx_temp[value]
        return idx
