from abc import ABC, abstractmethod
from functools import cache

from utils_future import Log

from ds.datumset.Datumset import Datumset
from ds.db.AbstractDB import AbstractDB
from ds.query.Query import Query

log = Log("AbstractGIGDB")


class AbstractGIGDB(AbstractDB, ABC):

    BASE_URL = (
        "https://raw.githubusercontent.com/nuuuwan/gig-data"
        "/refs/heads/master/gig2"
    )

    @classmethod
    @abstractmethod
    def get_metadata(cls):
        pass

    @classmethod
    @abstractmethod
    def get_datumset(cls, item) -> Datumset:
        pass

    @classmethod
    def is_metadata_item_matching_query(cls, item, query: Query):
        return (
            item["entity_class_name"] in query.entity_class_names
            and item["measurement_class_name"] in query.dim_labels
        )

    @classmethod
    @cache
    def get_metadata_for_query(cls, query_str):
        query = Query(query_str)
        metadata_for_query = []
        for item in cls.get_metadata():
            if cls.is_metadata_item_matching_query(item, query):
                metadata_for_query.append(item)
        log.debug(
            f"{len(metadata_for_query)} metadata items"
            + f" matched {query_str}"
        )
        return metadata_for_query

    @classmethod
    @cache
    def __class_getitem__(cls, query_str):
        query = Query(query_str)
        metadata_for_query = cls.get_metadata_for_query(query_str)
        datumset_list = [cls.get_datumset(item) for item in metadata_for_query]
        datum_list = []
        n_datum = 0
        n_datum_matching = 0
        for datumset in datumset_list:
            for datum in datumset:
                n_datum += 1
                if datum.is_match(query):
                    datum_list.append(datum)
                    n_datum_matching += 1
        datumset = Datumset(*datum_list)
        object.__setattr__(datumset, "_query_str", query_str)
        log.debug(
            f"Found {n_datum_matching}/{n_datum} matching datums"
            + f' for query "{query_str}"'
        )
        return datumset
