from abc import abstractmethod
from dataclasses import dataclass

from ds.measurement.Measurement import Measurement


@dataclass(frozen=True)
class CategoryMeasurement(Measurement):
    label: str

    @classmethod
    @abstractmethod
    def list(cls):
        pass

    @classmethod
    def idx(cls):
        return {m.label: m for m in cls.list()}

    @classmethod
    def from_label(cls, label: str):
        idx = cls.idx()
        if label not in idx:
            raise ValueError(f"Invalid label: {label}")
        return idx[label]

    @classmethod
    def __class_getitem__(cls, label: str):
        return cls.from_label(label)

    def to_data(self):
        return f'{self.__class__.__name__}:{self.label}'

    @classmethod
    def from_data(cls, data):
        return cls.from_label(data.split(':', 1)[1])
