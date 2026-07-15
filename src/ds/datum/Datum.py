from dataclasses import dataclass

from ds.datum.DatumMatchMixin import DatumMatchMixin
from ds.measurement.Measurement import Measurement
from ds.measurement.Time import Time


@dataclass(frozen=True)
class Datum(DatumMatchMixin):
    time: Time
    entity_class: type[Measurement]
    measurement_idx: dict[str, Measurement]

    def __init__(
        self,
        entity_class: type[Measurement],
        time: Time,
        **measurement_idx: Measurement,
    ):
        assert issubclass(entity_class, Measurement)
        object.__setattr__(self, 'entity_class', entity_class)
        assert isinstance(time, Time)
        object.__setattr__(self, 'time', time)
        object.__setattr__(self, 'measurement_idx', measurement_idx)

    def __hash__(self):
        return hash((self.time, frozenset(self.measurement_idx.items())))

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

    def to_json_inner(self, idx, measurement_part):
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
