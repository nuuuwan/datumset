from dataclasses import dataclass

from ds.datum.DatumMatchMixin import DatumMatchMixin
from ds.datum.DatumSerializeMixin import DatumSerializeMixin
from ds.measurement.District import District
from ds.measurement.House import House
from ds.measurement.Int import Int
from ds.measurement.Measurement import Measurement
from ds.measurement.Person import Person
from ds.measurement.Religion import Religion
from ds.measurement.Time import Time


class EntityFactory:
    @staticmethod
    def get(class_name: str):
        entity_class = dict(
            Religion=Religion,
            District=District,
            Person=Person,
            House=House,
            Int=Int,
        ).get(class_name)

        if not entity_class:
            raise ValueError(
                f"[EntityFactory] Unknown class_name: {class_name}"
            )
        return entity_class

    @staticmethod
    def from_value(data):
        class_name, _ = data.split(':', 1)
        cls = EntityFactory.get(class_name)
        return cls.from_data(data)


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

    def to_data(self):
        return dict(
            time=self.time.to_data(),
            entity_class=self.entity_class.__name__,
            measurement_idx={
                k: v.to_data() for k, v in self.measurement_idx.items()
            },
        )

    @classmethod
    def from_data(cls, data):
        time = Time.from_data(data['time'])
        entity_class = EntityFactory.get(data['entity_class'])
        measurement_idx = {
            k: EntityFactory.from_value(v)
            for k, v in data['measurement_idx'].items()
        }
        return cls(
            entity_class=entity_class,
            time=time,
            **measurement_idx,
        )
