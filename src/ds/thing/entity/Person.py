from dataclasses import dataclass

from ds.thing.entity.Entity import Entity


@dataclass(frozen=True)
class Person(Entity):
    id: str
    name: str
