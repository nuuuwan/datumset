from dataclasses import dataclass


@dataclass(frozen=True)
class Int:
    _value: int

    def __init__(self, value):
        object.__setattr__(self, '_value', int(value))

    def to_json(self):
        return self._value
