from functools import cache

from utils_future import JSONFile, Log

from ds.adapters.TSVAdapter import TSVAdapter
from ds.datumset.Datumset import Datumset
from ds.db.AbstractGIGDB import AbstractGIGDB
from ds.query.Query import Query
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory

log = Log("Elections")


class Elections(AbstractGIGDB):
    SKIP_KEYS = {
        "entity_id",
        "region_id",
        "valid",
        "rejected",
        "polled",
        "electors",
    }

    @classmethod
    def is_metadata_item_matching_query(  # noqa: C901,CFQ004
        cls, item, query: Query
    ):
        parent_check = (
            item["entity_class_name"] in query.entity_class_names
            and item["measurement_class_name"] in query.dim_labels
        )
        if not parent_check:
            return False

        query_time = query.dim_values_idx.get("Time")
        if query_time is not None:
            if item["year_id"] != query_time:
                return False

        election_type = query.dim_values_idx.get("ElectionType")
        if election_type is not None:
            if item["election_type_name"] != election_type:
                return False

        return True

    @classmethod
    def get_datumset(cls, item) -> Datumset:
        year_id = item["year_id"]
        measurement_id = item["measurement_id"]
        region_group_id = item["region_group_id"]
        entity_cls = ThingFactory[item["entity_class_name"]]
        measurement_cls = ThingFactory[item["measurement_class_name"]]
        et = ThingFactory["ElectionType"][item["election_type_name"]]
        time_concept = Time(year_id)
        extra_dims = {"ElectionType": et}
        url = (
            f"{cls.BASE_URL}"
            f"/{measurement_id}.{region_group_id}.{year_id}.tsv"
        )
        d_list = TSVAdapter.read(url)
        party = TSVAdapter.build_datumset(
            d_list,
            entity_cls,
            measurement_cls,
            cls.SKIP_KEYS,
            time_concept,
            extra_dims,
        )

        return Datumset(*list(party))

    @classmethod
    @cache
    def get_metadata(cls):
        return JSONFile("src", "ds", "db", "elections.metadata.json").read()
