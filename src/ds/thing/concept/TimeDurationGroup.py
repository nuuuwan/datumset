from dataclasses import dataclass

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class TimeDurationGroup(Concept):
    min_value: int
    max_value: int

    def __init__(self, min_value: int, max_value: int):
        if min_value > max_value:
            raise ValueError("min_value cannot be greater than max_value")
        object.__setattr__(self, "_value", f"{min_value}To{max_value}Years")
        object.__setattr__(self, "min_value", min_value)
        object.__setattr__(self, "max_value", max_value)

    @classmethod
    def from_value(cls, value: str) -> "TimeDurationGroup":
        tokens = value.replace("Years", "").split("To")

        if "OrMore" in tokens[0]:
            min_value = int(tokens[0].replace("OrMore", ""))
            max_value = float("inf")
        else:
            min_value = int(tokens[0])
            max_value = int(tokens[1])
        return cls(min_value, max_value)
