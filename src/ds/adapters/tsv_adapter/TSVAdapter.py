from utils_future import WWW, Directory, TSVFile

from ds.adapters.tsv_adapter.TSVAdapterBuildMixin import TSVAdapterBuildMixin
from ds.datumset.Datumset import Datumset


class TSVAdapter(TSVAdapterBuildMixin):
    TEMP_DIR = "gig2"

    @classmethod
    def read(cls, url) -> list:
        file_name = url.split("/")[-1]
        dir_temp = Directory.get_temp("datumset", cls.TEMP_DIR)
        dir_temp.make()
        tsv_file = TSVFile(dir_temp, file_name)
        WWW(url).download(tsv_file)
        d_list = tsv_file.read()
        d_list = [d for d in d_list if len(d["entity_id"]) != 10]
        return d_list

    @classmethod
    def load(
        cls,
        url,
        entity_cls,
        measurement_cls,
        skip_keys,
        time_concept,
        extra_dims=None,
    ) -> Datumset:
        return cls.build_datumset(
            cls.read(url),
            entity_cls,
            measurement_cls,
            skip_keys,
            time_concept,
            extra_dims,
        )
