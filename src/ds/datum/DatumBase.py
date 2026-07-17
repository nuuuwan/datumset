from dataclasses import dataclass

from ds.thing.concept.Concept import Concept
from ds.thing.entity.Entity import Entity


@dataclass
class DatumBase:
    entity_class: type[Concept]
    dim_idx: dict[str, Concept]
    cell_idx: dict[str, Concept]

    def __init__(
        self,
        entity_class: type[Concept],
        dim_idx: dict[str, Concept],
        cell_idx: dict[str, Concept],
    ):
        assert issubclass(entity_class, Entity)
        object.__setattr__(self, "entity_class", entity_class)
        object.__setattr__(self, "dim_idx", dim_idx)
        object.__setattr__(self, "cell_idx", cell_idx)

    def __hash__(self):
        return hash(
            (
                self.entity_class.__name__,
                tuple(self.dim_idx.items()),
                tuple(self.cell_idx.items()),
            )
        )
