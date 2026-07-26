from functools import cache

from utils_future import WWW, Directory, JSONFile, Log

from ds.datumset.Datumset import Datumset
from ds.db.AbstractDB import AbstractDB

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
    @cache
    def list(cls):
        datumset_list = []
        local_dir = Directory.get_temp("datumset", "census2024")

        for metadata in cls.metadata_idx():
            url = cls.URL_BASE + metadata + "/lanka_data.json"
            dataset_dir = Directory(local_dir, metadata)
            dataset_dir.make()
            local_data_file = JSONFile(dataset_dir, "lanka_data.json")
            WWW(url).download(local_data_file)
            datumset = Datumset.from_data(local_data_file.read())
            datumset_list.append(datumset)
        return datumset_list

    @classmethod
    def _get_local_data_file(cls, partial_path):
        url = cls.URL_BASE + partial_path
        local_dir = Directory.get_temp("datumset", "census2024")
        dataset_dir = Directory(local_dir, partial_path)
        local_data_file = JSONFile(dataset_dir, "lanka_data.json")

        if local_data_file.exists():
            return local_data_file

        dataset_dir.make()
        local_data_file = JSONFile(dataset_dir, "lanka_data.json")
        WWW(url).download(local_data_file)
        return local_data_file

    @classmethod
    @cache
    def __class_getitem__(cls, query_str):
        partial_paths_for_query = cls.metadata_idx().get(query_str, [])
        datumset = Datumset.empty()
        for partial_path in partial_paths_for_query:
            local_data_file = cls._get_local_data_file(partial_path)
            datumset_for_path = Datumset.from_data(local_data_file.read())
            datumset += datumset_for_path
        return datumset
