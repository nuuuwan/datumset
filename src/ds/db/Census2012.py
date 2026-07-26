from functools import cache

from utils_future import JSONFile, Log

from ds.adapters.TSVAdapter import TSVAdapter
from ds.datumset.Datumset import Datumset
from ds.db.AbstractDB import AbstractDB
from ds.query.Query import Query
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory

log = Log("Census2012")


class Census2012(AbstractDB):
    TIME = Time("2012")
    SKIP_KEYS = {
        "entity_id",
        "region_id",
    }
    BASE_URL = (
        "https://raw.githubusercontent.com/nuuuwan/gig-data"
        "/refs/heads/master/gig2"
    )

    @classmethod
    def get_datumset(
        cls,
        entity_class_name,
        measurement_class_name,
        measurement_id,
        region_group_id,
    ) -> Datumset:
        year_id = cls.TIME.get_value()
        entity_cls = ThingFactory[entity_class_name]
        measurement_cls = ThingFactory[measurement_class_name]
        url = (
            f"{cls.BASE_URL}"
            f"/{measurement_id}.{region_group_id}.{year_id}.tsv"
        )
        return TSVAdapter.load(
            url,
            entity_cls,
            measurement_cls,
            cls.SKIP_KEYS,
            Time(year_id),
        )

    @classmethod
    @cache
    def get_metadata(cls):
        return JSONFile("src", "ds", "db", "census2012.metadata.json").read()

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
        metadata_for_query = cls.get_metadata_for_query(query_str)
        datumset_list = [
            cls.get_datumset(
                item["entity_class_name"],
                item["measurement_class_name"],
                item["measurement_id"],
                item["region_group_id"],
            )
            for item in metadata_for_query
        ]
        datum_list = []
        for datumset in datumset_list:
            for datum in datumset:
                if query_str == datum.query.query_str:
                    datum_list.append(datum)
        return Datumset(*datum_list)
