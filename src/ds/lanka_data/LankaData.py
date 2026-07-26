from functools import cache

from ds.datumset.Datumset import Datumset
from ds.db.AbstractDB import AbstractDB
from ds.db.Census2012 import Census2012
# from ds.db.Census2024 import Census2024
from ds.db.Elections import Elections


class LankaData:

    @classmethod
    def get_db_class_List(cls) -> list[AbstractDB]:
        return [Census2012, Elections]

    @classmethod
    @cache
    def __class_getitem__(cls, query_str):
        datumset = Datumset.empty()
        for db_class in cls.get_db_class_List():
            datumset_for_db_class = db_class[query_str]
            datumset += datumset_for_db_class
        return datumset
