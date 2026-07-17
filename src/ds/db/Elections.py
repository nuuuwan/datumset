from functools import cache

from ds.adapters.TSVAdapter import TSVAdapter
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory
from utils_future import JSONFile


class Elections:
    BASE_URL = (
        "https://raw.githubusercontent.com/nuuuwan/gig-data"
        "/refs/heads/master/gig2"
    )
    SKIP_KEYS = {
        "entity_id",
        "region_id",
        "valid",
        "rejected",
        "polled",
        "electors",
    }

    @classmethod
    def get_datumset(cls, item) -> Datumset:
        year_id = item["year_id"]
        measurement_id = item["measurement_id"]
        region_group_id = item["region_group_id"]
        entity_cls = ThingFactory[item["entity_class_name"]]
        measurement_cls = ThingFactory[item["measurement_class_name"]]
        et = ThingFactory["ElectionType"][item["election_type_name"]]
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
            {"ElectionType": et},
        )

    @classmethod
    @cache
    def get_metadata(cls):
        return JSONFile("src", "ds", "db", "elections.metadata.json").read()

    @classmethod
    @cache
    def list(cls) -> list[Datumset]:
        return [cls.get_datumset(item) for item in cls.get_metadata()]
