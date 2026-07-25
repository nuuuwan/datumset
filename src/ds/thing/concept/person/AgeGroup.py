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
    def _has_total_terms(cls, value):
        for k in cls.TOTAL_WORDS:
            if k.lower() in value.lower():
                return True
        return False

    @classmethod
    def _has_more_terms(cls, value):
        for k in cls.MORE_WORDS:
            if k.lower() in value.lower():
                return True
        return False

    @classmethod
    def _has_less_terms(cls, value):
        for k in cls.LESS_WORDS:
            if k.lower() in value.lower():
                return True
        return False

    # flake8: noqa: C901
    @classmethod
    def from_value(cls, value):
        value = value.replace("-", "_")
        value = value.replace(" ", "_")

        if cls._has_total_terms(value):
            return cls(cls.MIN_TIME, cls.MAX_TIME)

        tokens = value.split("_")
        num_tokens = [int(token) for token in tokens if token.isdigit()]

        if cls._has_more_terms(value):
            return cls(int(num_tokens[0]), cls.MAX_TIME)

        if cls._has_less_terms(value):
            return cls(cls.MIN_TIME, int(num_tokens[0]))

        if len(num_tokens) == 1:
            common_value = int(num_tokens[0])
            return cls(common_value, common_value)

        return cls(int(num_tokens[0]), int(num_tokens[1]))
