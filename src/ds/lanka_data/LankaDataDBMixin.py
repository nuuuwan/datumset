from functools import cache

from ds.datum.Datum import Datum
from ds.db.Census2012 import Census2012


class LankaDataDBMixin:
    @classmethod
    @cache
    def idx(cls) -> dict[str, list[Datum]]:
        datumset_list = Census2012.list()
        idx = {}
        for datumset in datumset_list:
            for datum in datumset:
                query_str = datum.query.query_str
                if query_str not in idx:
                    idx[query_str] = []
                idx[query_str].append(datum)
        return idx
