from functools import cache

from ds.datumset.Datumset import Datumset
from ds.db.Census2012 import Census2012


class LankaDataDBMixin:
    @classmethod
    @cache
    def list(cls) -> list[Datumset]:
        return Census2012.list()
