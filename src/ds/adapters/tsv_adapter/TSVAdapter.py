from utils_future import WWW, Directory, TSVFile

from ds.adapters.tsv_adapter.TSVAdapterBuildMixin import TSVAdapterBuildMixin
from ds.datumset.Datumset import Datumset


class TSVAdapter(TSVAdapterBuildMixin):
    TEMP_DIR = "gig2"
    MIN_P = 0.001  # 0.1%

    @classmethod
    def compress(cls, d_list, skip_keys):
        # rows
        # HACK - Removed GNDs. Must be added back.
        row_compressed_list = [d for d in d_list if len(d["entity_id"]) != 10]

        # columns
        col_compressed_d_list = []

        for d in row_compressed_list:
            new_d = {}
            for k, v in d.items():
                if k in skip_keys and k != "entity_id":
                    continue
                if k.startswith("total_"):
                    continue
                new_d[k] = v
            col_compressed_d_list.append(new_d)

        d_lk = [d for d in col_compressed_d_list if d["entity_id"] == "LK"][0]
        values = {}
        for k, v in d_lk.items():
            if k == "entity_id":
                continue
            values[k] = float(v)

        total = sum(values.values())
        p_values = {k: v / total for k, v in values.items()}
        valid_keys = [k for k, v in p_values.items() if v >= cls.MIN_P]

        compress_d_list2 = []
        for d in col_compressed_d_list:
            new_d = {}
            for k, v in d.items():
                if k in valid_keys or k == "entity_id":
                    new_d[k] = v
            compress_d_list2.append(new_d)

        return compress_d_list2

    @classmethod
    def read(cls, url, skip_keys) -> list:
        file_name = url.split("/")[-1]
        dir_temp = Directory.get_temp("datumset", cls.TEMP_DIR)
        dir_temp.make()
        tsv_file = TSVFile(dir_temp, file_name)
        WWW(url).download(tsv_file)
        d_list = tsv_file.read()
        d_list = cls.compress(d_list, skip_keys)
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
            cls.read(url, skip_keys),
            entity_cls,
            measurement_cls,
            skip_keys,
            time_concept,
            extra_dims,
        )
