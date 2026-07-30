from dataclasses import dataclass

from ds.datum.Datum import Datum


@dataclass(frozen=True)
class DatumsetBase:
    _value: list[Datum]

    def __init__(self, _data: Datum):
        object.__setattr__(self, "_value", list(data))

    def __iter__(self):
        return iter(self._value)

    def __getitem__(self, index):
        return self._value[index]

    def __add__(self, other):
        cls = self.__class__
        if isinstance(other, cls):
            return cls(_(self._value + other._value))
        if isinstance(other, Datum):
            return cls(_(self._value + [other]))

        raise TypeError(
            "Unsupported operand type(s) for +:"
            + f" 'Datumset' and '{type(other).__name__}'"
        )

    def __len__(self):
        return len(self._value)

    @classmethod
    def empty(cls):
        return cls()
