from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.atom.Bool import Bool
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory
from utils_future import String


class DimToTimeToValueAdapter:

    @classmethod
    def _build_datum_list_from_d(
        cls,
        d,
        entity_cls,
        dim1_cls,
        dim1_class_key,
        value_label,
    ):
        dim1 = dim1_cls[String(d[dim1_class_key]).pascal]

        datum_list = []
        for k, v in d["values"].items():
            time_str = k.split("_")[-1]
            time = Time(time_str)
            datum = Datum(
                entity_cls,
                {
                    dim1_cls.__name__: dim1,
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
        dim1_class_name,
        dim1_class_key,
        value_label,
    ):
        entity_cls = ThingFactory[entity_class_name]
        dim1_cls = ThingFactory[dim1_class_name]

        datum_list = []
        for d in d_list:
            datum_list.extend(
                cls._build_datum_list_from_d(
                    d,
                    entity_cls,
                    dim1_cls,
                    dim1_class_key,
                    value_label,
                )
            )
        return Datumset(*datum_list)
