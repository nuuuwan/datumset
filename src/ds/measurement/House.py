from dataclasses import dataclass

from ds.measurement.Measurement import Measurement


@dataclass(frozen=True)
class House(Measurement):
    id: str
    address: str
