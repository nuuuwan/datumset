from abc import abstractmethod
from dataclasses import dataclass
from functools import cache

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class CategoryConcept(Concept):

    @classmethod
    @abstractmethod
    def list(cls):
        pass  # pragma: no cover

    @classmethod
    def idx(cls):
        return {m._value: m for m in cls.list()}

    @classmethod
    @cache
    def from_value(cls, value: str):
        idx = cls.idx()
        if value not in idx:
            raise ValueError(f"Invalid label: {value}")
        return idx[value]

    @classmethod
    def __class_getitem__(cls, value: str):
        return cls.from_value(value)
