from dataclasses import dataclass

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class TimeDurationGroup(Concept):
    min_value: int
    max_value: int

    def __init__(self, min_value: int, max_value: int):
        if min_value > max_value:
            raise ValueError("min_value cannot be greater than max_value")
        object.__setattr__(self, "_value", str([min_value, max_value]))
        object.__setattr__(self, "min_value", min_value)
        object.__setattr__(self, "max_value", max_value)
