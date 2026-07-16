from dataclasses import dataclass

from ds.thing.entity.Entity import Entity


@dataclass(frozen=True)
class House(Entity):
    id: str
    address: str

    def __init__(self, id: str, address: str):
        object.__setattr__(self, "_value", id)
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "address", address)
