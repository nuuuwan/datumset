from dataclasses import dataclass

from ds.thing.entity.Entity import Entity


@dataclass(frozen=True)
class Person(Entity):
    id: str
    name: str

    def __init__(self, id: str, name: str):
        Entity.__init__(self, id)
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)
