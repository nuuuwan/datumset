from dataclasses import dataclass

from ds.thing.concept.Concept import Concept
from ds.thing.concept.TimeDurationGroup import TimeDurationGroup


@dataclass(frozen=True)
class AgeGroup(Concept):

    MIN_TIME = TimeDurationGroup.MIN_TIME
    MAX_TIME = TimeDurationGroup.MAX_TIME
    MORE_WORDS = TimeDurationGroup.MORE_WORDS
    LESS_WORDS = TimeDurationGroup.LESS_WORDS

    TOTAL_WORDS = ["total", "sri_lanka"]

    def __init__(self, min_val: int, max_val: int):
        object.__setattr__(self, "_value", f"{min_val}To{max_val}Years")
        object.__setattr__(self, "min_val", min_val)
        object.__setattr__(self, "max_val", max_val)

    @classmethod
    def from_value(cls, value):
        value = value.replace("-", "_")
        value = value.replace(" ", "_")

        for k in cls.TOTAL_WORDS:
            if k.lower() in value.lower():
                min_value = cls.MIN_TIME
                max_value = cls.MAX_TIME
                return cls(min_value, max_value)

        tokens = value.split("_")
        num_tokens = [int(token) for token in tokens if token.isdigit()]

        for k in cls.MORE_WORDS:
            if k.lower() in value.lower():
                min_value = int(num_tokens[0])
                max_value = cls.MAX_TIME
                return cls(min_value, max_value)

        for k in cls.LESS_WORDS:
            if k.lower() in value.lower():
                min_value = cls.MIN_TIME
                max_value = int(num_tokens[0])
                return cls(min_value, max_value)

        if len(num_tokens) == 1:
            min_value = int(num_tokens[0])
            return cls(min_value, min_value)

        min_value = int(num_tokens[0])
        max_value = int(num_tokens[1])
        return cls(min_value, max_value)
