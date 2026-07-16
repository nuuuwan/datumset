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
        return dict(
            time=self.time.to_data(),
            entity_class=self.entity_class.__name__,
            concept_idx={k: v.to_data() for k, v in self.concept_idx.items()},
        )

    @classmethod
    def from_data(cls, data):
        time = Time.from_data(data["time"])
        entity_class = ThingFactory[data["entity_class"]]
        concept_idx = {
            k: ThingFactory.from_value(v)
            for k, v in data["concept_idx"].items()
        }
        return cls(
            entity_class=entity_class,
            time=time,
            **concept_idx,
        )
