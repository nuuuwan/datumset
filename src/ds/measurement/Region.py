from dataclasses import dataclass

from ds.measurement.CategoryMeasurement import CategoryMeasurement


@dataclass(frozen=True)
class Region(CategoryMeasurement):
    id: str
    name: str

    def __init__(self, id: str, name: str):
        object.__setattr__(self, 'label', id)
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'name', name)
