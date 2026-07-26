from abc import ABC, abstractmethod
from functools import cache

from ds.datumset.Datumset import Datumset


class AbstractDB(ABC):

    @classmethod
    @abstractmethod
    @cache
    def __class_getitem__(cls, query_str) -> Datumset:
        pass
