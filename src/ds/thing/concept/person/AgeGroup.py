from dataclasses import dataclass

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class AgeGroup(Concept):

    def __init__(self, min_val: int, max_val: int):
        object.__setattr__(self, "_value", str([min_val, max_val]))
        object.__setattr__(self, "min_val", min_val)
        object.__setattr__(self, "max_val", max_val)

    @classmethod
    def from_value(cls, value):
        value = value.replace("~", "-")
        value = value.replace(" ", "")
        parts = value.split("-")
        min_val, max_val = parts
        min_val = int(min_val)
        max_val = int(max_val)
        return cls(min_val, max_val)
