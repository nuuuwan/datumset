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
    def metadata_list(cls):
        WWW(cls.URL_LANKA_DATA_METADATA).download(cls.LANKA_DATA_METADATA_FILE)
        return cls.LANKA_DATA_METADATA_FILE.read()

    @classmethod
    @cache
    def list(cls):
        datumset_list = []
        local_dir = Directory.get_temp("datumset", "census2024")
        for metadata in cls.metadata_list():
            url = cls.URL_BASE + metadata + "/lanka_data.json"
            dataset_dir = Directory(local_dir, metadata)
            dataset_dir.make()
            local_data_file = JSONFile(dataset_dir, "lanka_data.json")
            WWW(url).download(local_data_file)
            datumset = Datumset.from_data(local_data_file.read())
            datumset_list.append(datumset)
        return datumset_list


if __name__ == "__main__":
    Census2024.list()
