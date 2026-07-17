from functools import cache

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Int import Int
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory
from utils_future import WWW, Directory, JSONFile, Log, String, TSVFile

log = Log("Census2012")


class Census2012:
    TIME = Time("2012")
    SKIP_KEYS = {"entity_id", "total_population", "region_id"}

    @classmethod
    def _get_datum_list_from_d(cls, d, entity_cls, col_map):
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
                {"Time": cls.TIME, r_name: region_instance, m_name: concept},
                {"Count": Int(int(float(d[k].strip().replace(",", ""))))},
            )
            for k, (m_name, concept) in col_map.items()
        ]

    @classmethod
    def get_datumset(
        cls,
        entity_class_name,
        measurement_class_name,
        measurement_id,
        region_group_id,
    ) -> Datumset:
        year_id = cls.TIME.get_value()
        entity_cls = ThingFactory[entity_class_name]
        measurement_cls = ThingFactory[measurement_class_name]

        url = (
            "https://raw.githubusercontent.com"
            + "/nuuuwan/gig-data/refs/heads/master"
            + f"/gig2/{measurement_id}.{region_group_id}.{year_id}.tsv"
        )

        tsv_file = TSVFile(
            Directory.get_temp("datumset", "census2012").path,
            f"{measurement_id}.{region_group_id}.{year_id}.tsv",
        )
        WWW(url).download(tsv_file)
        d_list = tsv_file.read()
        m_name = measurement_cls.__name__
        col_map = {
            k: (m_name, measurement_cls[String(k).pascal])
            for k in (d_list[0] if d_list else {})
            if k not in cls.SKIP_KEYS
        }
        datum_list = []
        for d in d_list:
            datum_list_for_d = cls._get_datum_list_from_d(
                d, entity_cls, col_map
            )
            if datum_list_for_d:
                datum_list.extend(datum_list_for_d)
        return Datumset(*datum_list)

    _list_cache = None

    @classmethod
    @cache
    def get_metadata(cls):
        return JSONFile("src", "ds", "db", "census2012.metadata.json").read()

    @classmethod
    def gen_list(cls):
        if cls._list_cache is None:
            result = []
            for item in cls.get_metadata():
                result.append(
                    cls.get_datumset(
                        item["entity_class_name"],
                        item["measurement_class_name"],
                        item["measurement_id"],
                        item["region_group_id"],
                    )
                )
            cls._list_cache = result
        yield from cls._list_cache
