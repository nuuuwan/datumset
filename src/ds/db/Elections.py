from functools import cache

from ds.datumset.Datumset import Datumset
from ds.db.Census2012 import Census2012
from utils_future import JSONFile


class Elections:
    @classmethod
    @cache
    def get_metadata(cls):
        return JSONFile("src", "ds", "db", "elections.metadata.json").read()

    @classmethod
    @cache
    def list(cls) -> list[Datumset]:
        return [
            Census2012.get_datumset(
                item["entity_class_name"],
                item["measurement_class_name"],
                item["measurement_id"],
                item["region_group_id"],
                item.get("year_id"),
                item.get("election_type_name"),
            )
            for item in cls.get_metadata()
        ]
