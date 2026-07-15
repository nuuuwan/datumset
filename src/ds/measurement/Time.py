from dataclasses import dataclass


@dataclass(frozen=True)
class Time:
    _value: str

    def is_match(self, query_str):
        return query_str == self._value

    def to_data(self):
        return f'{self.__class__.__name__}:{self._value}'

    @classmethod
    def from_data(cls, data):
        class_name, value = data.split(':', 1)
        assert class_name == cls.__name__
        return cls(value)
