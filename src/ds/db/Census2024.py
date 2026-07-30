from functools import cache

from utils_future import WWW, Directory, JSONFile, Log

from ds.datumset.Datumset import Datumset
from ds.db.AbstractDB import AbstractDB
from ds.query.Query import Query

log = Log("Census2024")


class Census2024(AbstractDB):
    URL_BASE = (
        "https://raw.githubusercontent.com"
        + "/nuuuwan/lk_census_2024/refs/heads/main/"
    )
    URL_LANKA_DATA_METADATA = URL_BASE + "metadata/lanka_data.metadata.json"

    LANKA_DATA_METADATA_FILE = JSONFile(
        "src", "ds", "db", "census2024.metadata.json"
    )

    @classmethod
    @cache
    def metadata_idx(cls):
        WWW(cls.URL_LANKA_DATA_METADATA).download(
            cls.LANKA_DATA_METADATA_FILE
        )
        return cls.LANKA_DATA_METADATA_FILE.read()

    @classmethod
    def _get_local_data_file(cls, partial_path):
        local_dir = Directory.get_temp("datumset", "census2024")
        local_dir.make()
        local_data_file = JSONFile(local_dir, partial_path)
        dataset_dir = local_data_file.get_parent_directory()

        if local_data_file.exists():
            return local_data_file

        url = cls.URL_BASE + partial_path
        dataset_dir.make()
        WWW(url).download(local_data_file)
        return local_data_file

    @classmethod
    @cache
    def __class_getitem__(cls, query_str):
        query = Query(query_str)
        partial_paths_for_query = cls.metadata_idx().get(
            query.base_query_str, []
        )
        datum_list = []
        for partial_path in partial_paths_for_query:
            local_data_file = cls._get_local_data_file(partial_path)
            datumset_for_path = Datumset.from_data(local_data_file.read())
            for datum in datumset_for_path:
                if datum.is_match(query):
                    datum_list.append(datum)
        return Datumset(_datum_list)
