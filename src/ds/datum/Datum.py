from dataclasses import dataclass

from ds.datum.DatumMatchMixin import DatumMatchMixin
from ds.thing.concept.Concept import Concept
from ds.thing.concept.Time import Time
from ds.thing.entity.Entity import Entity
from ds.thing.ThingFactory import ThingFactory
from utils_future import ShallowDict


@dataclass(frozen=True)
class Datum(DatumMatchMixin):
    entity_class: type[Concept]
    time: Time
    concept_idx: dict[str, Concept]

    def __init__(
        self,
        entity_class: type[Concept],
        time: Time,
        **concept_idx: Concept,
    ):
        assert issubclass(entity_class, Entity)
        object.__setattr__(self, "entity_class", entity_class)
        assert isinstance(time, Time)
        object.__setattr__(self, "time", time)
        object.__setattr__(self, "concept_idx", concept_idx)

    def __hash__(self):
        return hash((self.time, frozenset(self.concept_idx.items())))

    def to_data(self):
        nesting_values = [
            self.entity_class.__name__,
            self.time.get_value(),
        ] + list([v.to_kvpair() for v in self.concept_idx.values()])

        shallow_dict = ShallowDict()
        shallow_dict[tuple(nesting_values)] = 1
        return shallow_dict.to_deep()

    @classmethod
    def from_data(cls, data):
        shallow_d = ShallowDict.from_deep(data)
        key_tuple, _ = next(iter(shallow_d.items()))
        entity_class_name = key_tuple[0]
        time_value = key_tuple[1]
        time_data_item = {
            f"concept_{i}": v for i, v in enumerate(key_tuple[2:])
        }
        return cls.from_attributes(
            entity_class_name, time_value, time_data_item
        )

    @classmethod
    def from_attributes(cls, entity_class_name, time_value, time_data_item):
        concept_idx = {
            k: ThingFactory.from_kvpair(v) for k, v in time_data_item.items()
        }

        return cls(
            entity_class=ThingFactory[entity_class_name],
            time=Time.from_value(time_value),
            **concept_idx,
        )
