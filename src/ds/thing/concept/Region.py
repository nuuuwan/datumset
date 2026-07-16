from dataclasses import dataclass

from ds.thing.concept.CategoryConcept import CategoryConcept


@dataclass(frozen=True)
class Region(CategoryConcept):
    id: str
    name: str

    def __init__(self, id: str, name: str):
        object.__setattr__(self, 'label', id)
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'name', name)
