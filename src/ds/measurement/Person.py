from dataclasses import dataclass

from ds.measurement.Measurement import Measurement


@dataclass(frozen=True)
class Person(Measurement):
    id: str
    name: str
