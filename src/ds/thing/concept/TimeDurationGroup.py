from dataclasses import dataclass

from utils_future import Log

from ds.thing.concept.Concept import Concept

log = Log("TimeDurationGroup")


@dataclass(frozen=True)
class TimeDurationGroup(Concept):
    min_value: int
    max_value: int

    MORE_WORDS = ["more", "over", "greater", "than", "at least", "minimum"]
    LESS_WORDS = ["less", "under", "fewer", "than", "at most", "maximum"]
    MAX_TIME = 125
    MIN_TIME = 0

    def __init__(self, min_value: int, max_value: int):
        if min_value > max_value:
            raise ValueError("min_value cannot be greater than max_value")
        object.__setattr__(self, "_value", f"{min_value}To{max_value}Years")
        object.__setattr__(self, "min_value", min_value)
        object.__setattr__(self, "max_value", max_value)

    @staticmethod
    def _num_part_(value: str) -> list[int]:
        tokens = value.split("_")
        num_tokens = [int(token) for token in tokens if token.isdigit()]
        return num_tokens

    # flake8: noqa: C901
    @classmethod
    def from_value(cls, value: str) -> "TimeDurationGroup":
        value = value.replace("To", "_")
        tokens = value.split("_")
        num_tokens = [int(token) for token in tokens if token.isdigit()]

        for k in cls.MORE_WORDS:
            if k in value:
                min_value = num_tokens[0]
                max_value = cls.MAX_TIME
                return cls(min_value, max_value)

        for k in cls.LESS_WORDS:
            if k in value:
                min_value = cls.MIN_TIME
                max_value = num_tokens[0]
                return cls(min_value, max_value)

        if len(num_tokens) >= 2:
            min_value = int(num_tokens[0])
            max_value = int(num_tokens[1])
            return cls(min_value, max_value)

        log.debug(f"{tokens=}")
        log.debug(f"{num_tokens=}")
        raise ValueError(f"Cannot parse TimeDurationGroup from value: {value}")
