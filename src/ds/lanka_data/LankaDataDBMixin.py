from functools import cache

from utils_future import Log

from ds.datum.Datum import Datum
from ds.db.Census2012 import Census2012
from ds.db.Census2024 import Census2024
from ds.db.Elections import Elections

log = Log("LankaDataDBMixin")


class LankaDataDBMixin:

    @classmethod
    def get_db_class_List(cls):
        return [Census2012, Elections, Census2024]

    @classmethod
    @cache
    def idx(cls) -> dict[str, list[Datum]]:
        datumset_list = []
        for db_cls in cls.get_db_class_List():
            datumset_list_for_db_cls = db_cls.list()
            log.debug(
                f"Loaded {len(datumset_list_for_db_cls)}"
                + f" datumsets from {db_cls.__name__}"
            )
            datumset_list.extend(datumset_list_for_db_cls)

        idx = {}
        for datumset in datumset_list:
            for datum in datumset:
                query_str = datum.query.query_str
                if query_str not in idx:
                    idx[query_str] = []
                idx[query_str].append(datum)
        return idx
