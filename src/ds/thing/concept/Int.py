from dataclasses import dataclass


@dataclass(frozen=True)
class Int:
    _value: int

    def __init__(self, value):
        object.__setattr__(self, "_value", int(value))

    def to_data(self):
        return f"{self.__class__.__name__}:{self._value}"

    @classmethod
    def from_data(cls, data):
        return cls(int(data.split(":", 1)[1]))

    def is_match(self, query_str):
        return query_str == self._value
