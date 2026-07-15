from dataclasses import dataclass


@dataclass(frozen=True)
class Time:
    _value: str

    def is_match(self, query_str):
        return query_str == self._value
