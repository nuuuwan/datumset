from dataclasses import dataclass

from ds.datum.DatumMatchMixin import DatumMatchMixin
from ds.datum.DatumSerializeMixin import DatumSerializeMixin
from ds.measurement.Measurement import Measurement
from ds.measurement.Time import Time


@dataclass(frozen=True)
class Datum(DatumMatchMixin, DatumSerializeMixin):
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
