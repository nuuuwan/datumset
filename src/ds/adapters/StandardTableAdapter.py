from utils_future import Log

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory

log = Log("StandardTableAdapter")


class StandardTableAdapter:

    @classmethod
    def _get_datum_list_from_d(
        cls,
        d,
        entity_cls,
        time,
        row_dim_cls,
        row_dim_key,
        col_dim_cls,
        cell_label,
        cell_cls,
    ):
        row_value = d[row_dim_key]
        try:
            row_dim_instance = row_dim_cls.from_value(row_value)
        except ValueError as e:
            try:
                row_dim_instance = row_dim_cls.from_value(row_value)
            except ValueError as e2:
                log.warning(f'Failed to create "{row_value}": {e}/{e2}')
                return []

        datum_list = []
        for k, v in d["values"].items():
            if "total" in k.lower():
                continue
            if k.startswith("p_"):
                k = k[2:]
            if col_dim_cls:
                col_dim_instance = (
                    ThingFactory.from_kvpair(k)
                    if ":" in k
                    else col_dim_cls.from_value(k)
                )
            cell_instance = cell_cls.from_value(v)

            dim_idx = {}
            if time is not None:
                dim_idx["Time"] = time

            dim_idx[row_dim_cls.__name__] = row_dim_instance
            if col_dim_cls:
                dim_idx[col_dim_cls.__name__] = col_dim_instance

            datum = Datum(
                entity_cls,
                dim_idx,
                {cell_label: cell_instance},
            )
            datum_list.append(datum)
        return datum_list

    @classmethod
    def build_datumset(
        cls,
        d_list,
        entity_class_name,
        time_value,
        row_dim_class_name,
        row_dim_key,
        col_dim_class_name,
        cell_label,
        cell_class_name,
    ):

        entity_cls = ThingFactory[entity_class_name]
        row_dim_cls = ThingFactory[row_dim_class_name]
        col_dim_cls = (
            ThingFactory[col_dim_class_name]
            if not col_dim_class_name.startswith("<")
            else None
        )
        cell_cls = ThingFactory[cell_class_name]
        time = (
            Time.from_value(time_value)
            if not time_value.startswith("<")
            else None
        )

        datum_list = []
        for d in d_list:
            datum_list_for_d = cls._get_datum_list_from_d(
                d,
                entity_cls,
                time,
                row_dim_cls,
                row_dim_key,
                col_dim_cls,
                cell_label,
                cell_cls,
            )
            datum_list.extend(datum_list_for_d)

        return Datumset(*datum_list)
