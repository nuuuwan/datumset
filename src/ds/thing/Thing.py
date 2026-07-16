from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class Thing(ABC):
    _value: str

    def __init__(self, _value):
        object.__setattr__(self, "_value", str(_value))

    @classmethod
    def is_class_match(cls, query_str):
        return query_str == cls.__name__

    def is_match(self, query_str):
        return query_str == self._value

    def to_data(self):
        return f"{self.__class__.__name__}:{self._value}"

    @classmethod
    def from_data(cls, data):
        return cls(data)
