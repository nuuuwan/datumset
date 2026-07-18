from dataclasses import dataclass

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class AgeGroup(Concept):

    def __init__(self, min_val: int, max_val: int):
        object.__setattr__(self, "_value", f"{min_val}To{max_val}Years")
        object.__setattr__(self, "min_val", min_val)
        object.__setattr__(self, "max_val", max_val)

    @classmethod
    def from_value(cls, value):
        if "total" in value.lower():
            return cls(0, 125)
        tokens = value.split(" ")
        num_tokens = [t for t in tokens if t.isnumeric()]

        if len(num_tokens) == 2:
            return cls(int(num_tokens[0]), int(num_tokens[1]))
        if len(num_tokens) == 1:
            if "less" in value.lower() or "under" in value.lower():
                return cls(0, int(num_tokens[0]))
            if "more" in value.lower() or "over" in value.lower():
                return cls(int(num_tokens[0]), 125)

        raise ValueError(f"Cannot parse AgeGroup from value: {value}")
