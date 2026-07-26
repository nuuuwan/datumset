from abc import ABC, abstractmethod

from ds.datumset.Datumset import Datumset


class AbstractDB(ABC):
    @classmethod
    @abstractmethod
    def list(cls) -> list[Datumset]:
        raise NotImplementedError
