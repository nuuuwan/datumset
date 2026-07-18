from utils_future import String

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.ThingFactory import ThingFactory


class GenericValueAdapter:

    @classmethod
    def _build_datum_list_from_d(cls, d, entity_cls, dim_idx, cell_idx):

        datum_dim_idx = {}
        for k, v in d.items():
            if k == "values":
                continue
            v = v.replace("*", "")

            if v == "Sri Lanka":
                continue

            v = String(v).pascal

            for dim_class_name, dim_key in dim_idx.items():
                if dim_key == k:
                    dim_cls = ThingFactory[dim_class_name]
                    datum_dim_idx[dim_cls.__name__] = (
                        dim_cls[v]
                        if dim_class_name not in ["Time"]
                        else dim_cls(v)
                    )

        if not datum_dim_idx:
            return []

        datum_cell_idx = {}
        for k, v in d["values"].items():
            for value_class_name_and_label, value_key in cell_idx.items():
                value_class_name, value_class_label = (
                    value_class_name_and_label.split(":")
                )
                if value_key == k:
                    value_cls = ThingFactory[value_class_name]
                    datum_cell_idx[value_class_label] = value_cls(v)
        return [Datum(entity_cls, datum_dim_idx, datum_cell_idx)]

    @classmethod
    def build_datumset(cls, d_list, entity_class_name, dim_idx, cell_idx):
        entity_cls = ThingFactory[entity_class_name]

        datum_list = []
        for d in d_list:
            datum_list.extend(
                cls._build_datum_list_from_d(d, entity_cls, dim_idx, cell_idx)
            )
        return Datumset(*datum_list)
