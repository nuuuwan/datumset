from typing import Generator

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Int import Int
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory
from utils_future import WWW, Directory, Log, String, TSVFile

log = Log("Census2012")


class Census2012:
    TIME = Time("2012")

    @classmethod
    def _get_datum_list_from_d(cls, d, entity_cls, measurement_cls):
        region_id = d["entity_id"]
        try:
            region_cls = RegionFactory.from_region_id(region_id)
        except ValueError:
            return None
        region_cls_name = region_cls.__name__
        try:
            region_instance = region_cls[region_id]
        except ValueError:
            return None
        measurement_cls_name = measurement_cls.__name__
        skip = {"entity_id", "total_population", "region_id"}

        datum_list = []
        for k, v in d.items():
            if k in skip:
                continue
            datum = Datum(
                entity_cls,
                {
                    "Time": cls.TIME,
                    region_cls_name: region_instance,
                    measurement_cls_name: measurement_cls[String(k).pascal],
                },
                dict(Count=Int(String(v).int)),
            )
            datum_list.append(datum)
        return datum_list

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
        datum_list = []
        d_list = tsv_file.read()
        for d in d_list:
            datum_list_for_d = cls._get_datum_list_from_d(
                d, entity_cls, measurement_cls
            )
            if datum_list_for_d:
                datum_list.extend(datum_list_for_d)
        return Datumset(*datum_list)

    _list_cache = None

    @classmethod
    def gen_list(cls) -> Generator[Datumset, None, None]:
        if cls._list_cache is not None:
            return cls._list_cache
        for (
            entity_class_name,
            measurement_class_name,
            measurement_id,
            region_group_id,
        ) in [
            ["Person", "Religion", "population-religion", "regions"],
            [
                "Person",
                "IsEconomicallyActive",
                "economy-economic-activity",
                "regions",
            ],
            ["Person", "Ethnicity", "population-ethnicity", "regions"],
        ]:
            datumset = cls.get_datumset(
                entity_class_name,
                measurement_class_name,
                measurement_id,
                region_group_id,
            )
            yield datumset
