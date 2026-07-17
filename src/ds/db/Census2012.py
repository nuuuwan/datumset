from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Int import Int
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.Religion import Religion
from ds.thing.concept.Time import Time
from ds.thing.entity.Person import Person
from utils_future import WWW, Directory, String, TSVFile


class Census2012:
    ENTITY_CLASS = Person
    TIME = Time("2012")

    @classmethod
    def get_datum_list_from_d(cls, d):
        region_id = d["entity_id"]
        try:
            region_cls = RegionFactory.from_region_id(region_id)
        except Exception:
            return None

        region_cls_name = region_cls.__name__

        datum_list = []
        for k, v in d.items():
            if k in ["entity_id", "total_population"]:
                continue
            concept_name = String(k).pascal

            datum = Datum(
                cls.ENTITY_CLASS,
                {
                    "Time": cls.TIME,
                    f"{region_cls_name}": region_cls[region_id],
                    "Religion": Religion[concept_name],
                },
                dict(Count=Int(String(v).int)),
            )
            datum_list.append(datum)
        return datum_list

    @classmethod
    def get_religion(cls) -> Datumset:
        measurement_id = "population-religion"
        region_id = "regions"
        year_id = cls.TIME.get_value()
        url = (
            "https://raw.githubusercontent.com"
            + "/nuuuwan/gig-data/refs/heads/master"
            + f"/gig2/{measurement_id}.{region_id}.{year_id}.tsv"
        )

        tsv_file = TSVFile(
            Directory.get_temp("datumset", "census2012").path,
            f"{measurement_id}.{region_id}.{year_id}.tsv",
        )
        WWW(url).download(tsv_file)
        datum_list = []
        d_list = tsv_file.read()
        for d in d_list:
            datum_list_for_d = cls.get_datum_list_from_d(d)
            if datum_list_for_d:
                datum_list.extend(datum_list_for_d)
        return Datumset(*datum_list)

    @classmethod
    def list(cls) -> list[Datumset]:
        return [cls.get_religion()]
