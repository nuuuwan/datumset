from functools import cache

from ds.adapters.TSVAdapter import TSVAdapter
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory
from utils_future import JSONFile


class Census2012:
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
    @cache
    def list(cls):
        return [
            cls.get_datumset(
                item["entity_class_name"],
                item["measurement_class_name"],
                item["measurement_id"],
                item["region_group_id"],
            )
            for item in cls.get_metadata()
        ]
