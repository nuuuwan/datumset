from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.atom.Int import Int
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory
from utils_future import String


class RegionValueAdapter:
    @classmethod
    def _build_datum_list_from_d(
        cls, d, entity_cls, time_concept, measurement_cls, region_id_field
    ):
        region_id = d[region_id_field]
        try:
            region_cls = RegionFactory.from_region_id(region_id)
            region_instance = region_cls[region_id]
        except ValueError:
            return []
        r_name = region_cls.__name__
        m_name = measurement_cls.__name__
        return [
            Datum(
                entity_cls,
                {
                    "Time": time_concept,
                    r_name: region_instance,
                    m_name: measurement_cls[String(k).pascal],
                },
                {"Count": Int(v)},
            )
            for k, v in d["values"].items()
        ]

    @classmethod
    def build_datumset(
        cls,
        d_list,
        entity_class_name,
        time_str,
        measurement_class_name,
        region_id_field="region_id",
    ) -> Datumset:
        time_concept = Time(str(time_str))
        datum_list = []
        entity_cls = ThingFactory[entity_class_name]
        measurement_cls = ThingFactory[measurement_class_name]
        for d in d_list:
            datum_list.extend(
                cls._build_datum_list_from_d(
                    d,
                    entity_cls,
                    time_concept,
                    measurement_cls,
                    region_id_field,
                )
            )
        return Datumset(*datum_list)
