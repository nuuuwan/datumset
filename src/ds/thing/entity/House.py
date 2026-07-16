from dataclasses import dataclass

from ds.thing.entity.Entity import Entity


@dataclass(frozen=True)
class House(Entity):
    id: str
    address: str
