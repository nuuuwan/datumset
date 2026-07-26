from functools import cache

from utils_future import JSONFile, Log

from ds.adapters.TSVAdapter import TSVAdapter
from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.db.AbstractDB import AbstractDB
from ds.query.Query import Query
from ds.thing.concept.atom.Int import Int
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory

log = Log("Elections")


class Elections(AbstractDB):
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
    TURNOUT_COLS = ["electors", "polled", "valid", "rejected"]

    @classmethod
    def _build_turnout_datum(cls, d, entity_cls, time_concept, extra_dims):
        region_id = d["entity_id"]
        try:
            region_cls = RegionFactory.from_region_id(region_id)
            region_instance = region_cls[region_id]
        except ValueError:
            return None
        r_name = region_cls.__name__
        return Datum(
            entity_cls,
            {
                **extra_dims,
                "Time": time_concept,
                r_name: region_instance,
            },
            {
                k: Int(
                    int(float(d.get(k, "0").strip().replace(",", "") or "0"))
                )
                for k in cls.TURNOUT_COLS
                if k in d
            },
        )

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
        turnout = [
            cls._build_turnout_datum(d, entity_cls, time_concept, extra_dims)
            for d in d_list
        ]
        return Datumset(*list(party) + [t for t in turnout if t])

    @classmethod
    @cache
    def get_metadata(cls):
        return JSONFile("src", "ds", "db", "elections.metadata.json").read()

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
        datumset_list = [cls.get_datumset(item) for item in metadata_for_query]
        datum_list = []
        for datumset in datumset_list:
            for datum in datumset:
                if query_str == datum.query.query_str:
                    datum_list.append(datum)
        log.debug(f'{len(datum_list)} datums matched "{query_str}"')
        return Datumset(*datum_list)
