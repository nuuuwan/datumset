from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class Thing(ABC):
    _value: str

    def __init__(self, _value):
        object.__setattr__(self, "_value", str(_value))

    def to_kvpair(self):
        return f"{self.__class__.__name__}:{self._value}"

    @classmethod
    def from_value(cls, value):
        return cls(value)

    def get_value(self):
        return self._value
