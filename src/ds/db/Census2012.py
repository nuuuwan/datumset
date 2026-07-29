from functools import cache

from utils_future import JSONFile, Log

from ds.adapters.tsv_adapter.TSVAdapter import TSVAdapter
from ds.datumset.Datumset import Datumset
from ds.db.AbstractGIGDB import AbstractGIGDB
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory

log = Log("Census2012")


class Census2012(AbstractGIGDB):

    SKIP_KEYS = {
        "entity_id",
        "region_id",
    }

    @classmethod
    def get_datumset(cls, item) -> Datumset:

        entity_class_name = item["entity_class_name"]
        measurement_class_name = item["measurement_class_name"]
        measurement_id = item["measurement_id"]
        region_group_id = item["region_group_id"]

        year_id = Time("2012").get_value()
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
