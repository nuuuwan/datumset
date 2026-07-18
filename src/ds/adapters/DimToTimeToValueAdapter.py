from utils_future import String

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.atom.Bool import Bool
from ds.thing.concept.region.Region import Region
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory


class DimToTimeToValueAdapter:

    @classmethod
    def _build_datum_list_from_d(
        cls,
        d,
        entity_cls,
        dim_cls,
        dim_class_key,
        value_label,
    ):
        dim1_value = d[dim_class_key]
        if not issubclass(dim_cls, Region):
            dim1_value = String(dim1_value).pascal
        if dim1_value in ["SriLanka"]:
            return []

        dim1 = dim_cls[dim1_value]

        datum_list = []
        for k, v in d["values"].items():
            time_str = k.split("_")[-1]
            time = Time(time_str)
            datum = Datum(
                entity_cls,
                {
                    dim_cls.__name__: dim1,
                    "Time": time,
                },
                {value_label: Bool(v)},
            )
            datum_list.append(datum)
        return datum_list

    @classmethod
    def build_datumset(
        cls,
        d_list,
        entity_class_name,
        dim_class_name,
        dim_class_key,
        value_label,
    ):
        entity_cls = ThingFactory[entity_class_name]
        dim_cls = ThingFactory[dim_class_name]

        datum_list = []
        for d in d_list:
            datum_list.extend(
                cls._build_datum_list_from_d(
                    d,
                    entity_cls,
                    dim_cls,
                    dim_class_key,
                    value_label,
                )
            )
        return Datumset(*datum_list)
