from abc import abstractmethod
from dataclasses import dataclass
from functools import cache

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class CategoryConcept(Concept):

    @classmethod
    @cache
    @abstractmethod
    def list(cls):
        pass  # pragma: no cover

    @classmethod
    @cache
    def idx(cls):
        return {m._value: m for m in cls.list()}

    @classmethod
    @cache
    def map_alias(cls, value):
        return value

    @classmethod
    @cache
    def from_value(cls, value: str):
        value = value.replace("Population", "")
        value = cls.map_alias(value)
        idx = cls.idx()
        if value not in idx:
            raise ValueError(
                f"Invalid label: {value} for {cls.__name__}."
                + f" Valid labels: {list(idx.keys())}"
            )
        return idx[value]

    @classmethod
    @cache
    def __class_getitem__(cls, value: str):
        return cls.from_value(value)
