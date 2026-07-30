from functools import cache

from utils_future import Log

from ds.datumset.Datumset import Datumset
from ds.db.AbstractDB import AbstractDB
from ds.db.Census2012 import Census2012
from ds.db.Census2024 import Census2024
from ds.db.Elections import Elections
from ds.query.DerivedQuery import DerivedQuery

log = Log("LankaData")


class LankaData:

    @classmethod
    def get_db_class_List(cls) -> list[AbstractDB]:
        return [Census2012, Elections, Census2024]

    @classmethod
    @cache
    def __class_getitem__(cls, query_str):
        if DerivedQuery.is_derived(query_str):
            return DerivedQuery[query_str]

        datumset = Datumset.empty()
        for db_class in cls.get_db_class_List():
            datumset_for_db_class = db_class[query_str]
            if len(datumset_for_db_class) > 0:
                log.debug(
                    f"{len(datumset_for_db_class)} datums"
                    + f" from {db_class.__name__}"
                    + f' for query "{query_str}"'
                )
            datumset += datumset_for_db_class
        object.__setattr__(datumset, "_query_str", query_str)
        return datumset
