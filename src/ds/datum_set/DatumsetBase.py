from dataclasses import dataclass

from ds.datum.Datum import Datum


@dataclass(frozen=True)
class DatumsetBase:
    _value: list[Datum]

    def __init__(self, *data: Datum):
        object.__setattr__(self, "_value", set(data))
