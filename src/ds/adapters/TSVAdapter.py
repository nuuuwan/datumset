from utils_future import WWW, Directory, String, TSVFile

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.atom.Int import Int
from ds.thing.concept.region.RegionFactory import RegionFactory


class TSVAdapter:
    TEMP_DIR = "gig2"

    @classmethod
    def _build_col_map(cls, d_list, measurement_cls, skip_keys):
        m_name = measurement_cls.__name__
        use_raw = getattr(measurement_cls, "RAW_COLUMNS", False)
        return {
            k: (m_name, measurement_cls[k if use_raw else String(k).pascal])
            for k in (d_list[0] if d_list else {})
            if k not in skip_keys
            and not k.startswith("total_")
            and ":" not in k
        }

    @classmethod
    def _get_datum_list_from_d(
        cls, d, entity_cls, col_map, time_concept, extra_dims
    ):
        region_id = d["entity_id"]
        try:
            region_cls = RegionFactory.from_region_id(region_id)
            region_instance = region_cls[region_id]
        except ValueError:
            return None
        r_name = region_cls.__name__
        return [
            Datum(
                entity_cls,
                {
                    **(extra_dims or {}),
                    "Time": time_concept,
                    r_name: region_instance,
                    m_name: concept,
                },
                {
                    "Count": Int(
                        int(float(d[k].strip().replace(",", "") or "0"))
                    )
                },
            )
            for k, (m_name, concept) in col_map.items()
        ]

    @classmethod
    def read(cls, url) -> list:
        file_name = url.split("/")[-1]
        tsv_file = TSVFile(
            Directory.get_temp("datumset", cls.TEMP_DIR).path,
            file_name,
        )
        WWW(url).download(tsv_file)
        return tsv_file.read()

    @classmethod
    def build_datumset(
        cls,
        d_list,
        entity_cls,
        measurement_cls,
        skip_keys,
        time_concept,
        extra_dims=None,
    ) -> Datumset:
        col_map = cls._build_col_map(d_list, measurement_cls, skip_keys)
        datum_list = []
        for d in d_list:
            rows = cls._get_datum_list_from_d(
                d, entity_cls, col_map, time_concept, extra_dims
            )
            if rows:
                datum_list.extend(rows)
        return Datumset(*datum_list)

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
