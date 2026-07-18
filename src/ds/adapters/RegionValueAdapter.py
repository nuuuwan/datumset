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
        cls,
        d,
        entity_cls,
        time_concept,
        measurement_cls,
        region_id_field,
        value_label,
        value_cls,
    ):
        region_id = d[region_id_field]
        try:
            region_cls = RegionFactory.from_region_id(region_id)
            region_instance = region_cls[region_id]
        except ValueError:
            return []
        r_name = region_cls.__name__
        m_name = measurement_cls.__name__ if measurement_cls else ""

        datum_list = []
        for k, v in d["values"].items():
            dim_idx = {
                "Time": time_concept,
                r_name: region_instance,
            }
            if measurement_cls:
                if measurement_cls == Time:
                    dim_idx[m_name] = Time(k.split("_")[-1])
                else:
                    dim_idx[m_name] = measurement_cls[String(k).pascal]
            datum = Datum(
                entity_cls,
                dim_idx,
                {value_label: value_cls(v)},
            )
            datum_list.append(datum)
        return datum_list

    @classmethod
    def build_datumset(
        cls,
        d_list,
        entity_class_name,
        time_str,
        measurement_class_name,
        region_id_field=None,
        value_label=None,
        value_class_name=None,
    ) -> Datumset:
        time_concept = Time(str(time_str))
        datum_list = []
        entity_cls = ThingFactory[entity_class_name]
        measurement_cls = (
            ThingFactory[measurement_class_name]
            if measurement_class_name != ""
            else None
        )

        region_id_field = region_id_field or "region_id"
        value_label = value_label or "Count"
        value_class_name = value_class_name or "Int"

        value_cls = ThingFactory[value_class_name]
        for d in d_list:
            datum_list.extend(
                cls._build_datum_list_from_d(
                    d,
                    entity_cls,
                    time_concept,
                    measurement_cls,
                    region_id_field,
                    value_label,
                    value_cls,
                )
            )
        return Datumset(*datum_list)
