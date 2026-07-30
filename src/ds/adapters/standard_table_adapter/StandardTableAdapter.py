from ds.adapters.standard_table_adapter.StandardTableAdapterDatumMixin import \
    StandardTableAdapterDatumMixin
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Time import Time
from ds.thing.ThingFactory import ThingFactory


class StandardTableAdapter(StandardTableAdapterDatumMixin):

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

        return Datumset(_datum_list)
