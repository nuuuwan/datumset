from abc import abstractmethod
from dataclasses import dataclass
from functools import cache

from utils_future import String

from ds.thing.concept.Concept import Concept


@dataclass(frozen=True)
class CategoryConcept(Concept):

    @classmethod
    @cache
    @abstractmethod
    def valid_values(cls) -> list[str]:
        pass  # pragma: no cover

    @classmethod
    def list(cls):
        return [cls(value) for value in cls.valid_values()]

    @classmethod
    @cache
    def idx(cls):
        return {m._value: m for m in cls.list()}

    @classmethod
    @cache
    def map_alias(cls):
        return {}

    @classmethod
    @cache
    def _check_map_alias(cls):
        valid_values = cls.valid_values()
        for valid_value in cls.map_alias():
            if valid_value not in valid_values:
                raise ValueError(
                    f"Invalid map_alias key: {valid_value}"
                    + f" for {cls.__name__}."
                    + f" Valid values: {valid_values}"
                )

    @classmethod
    @cache
    def _alias_to_value(cls):
        idx = {}
        for valid_value, aliases in cls.map_alias().items():
            for alias in aliases:
                idx[alias] = valid_value
        return idx

    @classmethod
    @cache
    def from_value(cls, value: str):
        cls._check_map_alias()
        value = value.replace("*", "")
        value = String(value).snake
        value = value.lower()
        value = cls._alias_to_value().get(value, value)

        idx = cls.idx()
        if value in idx:
            return idx[value]

        raise ValueError(
            f"Invalid label: {value} for {cls.__name__}."
            + f" Valid labels: {list(idx.keys())}"
        )

    @classmethod
    @cache
    def __class_getitem__(cls, value: str):
        return cls.from_value(value)

    @classmethod
    @cache
    def is_ordered(cls):
        return False
