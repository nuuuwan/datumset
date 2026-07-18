from utils_future import String

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.atom.Int import Int
from ds.thing.concept.region.Region import Region
from ds.thing.ThingFactory import ThingFactory


class DimToValueAdapter:

    @classmethod
    def _build_datum_list_from_d(
        cls,
        d,
        entity_cls,
        dim_cls,
        dim_class_key,
        value_cls,
        value_label,
    ):
        dim_value = d[dim_class_key]
        if dim_value == "Total":
            return []

        if not issubclass(dim_cls, Region):
            dim_value = String(dim_value).pascal
        dim = dim_cls[dim_value]

        datum_list = []
        for k, v in d["values"].items():
            datum = Datum(
                entity_cls,
                {dim_cls.__name__: dim, value_label: value_cls(k)},
                {"Count": Int(v)},
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
        value_class_name,
        value_label,
    ):
        entity_cls = ThingFactory[entity_class_name]
        dim_cls = ThingFactory[dim_class_name]
        value_cls = ThingFactory[value_class_name]

        datum_list = []
        for d in d_list:
            datum_list.extend(
                cls._build_datum_list_from_d(
                    d,
                    entity_cls,
                    dim_cls,
                    dim_class_key,
                    value_cls,
                    value_label,
                )
            )
        return Datumset(*datum_list)
