from dataclasses import dataclass

from ds.thing.concept.Concept import Concept
from ds.thing.concept.Time import Time
from ds.thing.entity.Entity import Entity


@dataclass
class DatumBase:
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
