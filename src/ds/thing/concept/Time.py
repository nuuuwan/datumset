from dataclasses import dataclass

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class Time(Concept):
    @classmethod
    def from_value(cls, value: str) -> "Time":
        return cls(value[-4:])
