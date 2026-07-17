from typing import Generator

from ds.datumset.Datumset import Datumset
from ds.db.Census2012 import Census2012


class LankaDataDBMixin:
    @classmethod
    def gen_list(cls) -> Generator[Datumset, None, None]:
        yield from Census2012.gen_list()
