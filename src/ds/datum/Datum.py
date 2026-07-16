from dataclasses import dataclass

from ds.datum.DatumMatchMixin import DatumMatchMixin
from ds.thing.concept.Concept import Concept
from ds.thing.concept.Time import Time
from ds.thing.entity.Entity import Entity
from ds.thing.ThingFactory import ThingFactory


@dataclass(frozen=True)
class Datum(DatumMatchMixin):
    time: Time
    entity_class: type[Concept]
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

        return {
            self.entity_class.__name__: {
                self.time.get_value(): {
                    k: v.to_kvpair() for k, v in self.concept_idx.items()
                }
            }
        }

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
