from ds.adapters.standard_table_adapter.StandardTableAdapterRowMixin import \
    StandardTableAdapterRowMixin
from ds.datum.Datum import Datum


class StandardTableAdapterDatumMixin(StandardTableAdapterRowMixin):

    @classmethod
    def _get_datum_from_kv(
        cls,
        k,
        v,
        entity_cls,
        time,
        row_dim_cls,
        row_dim_instance,
        col_dim_cls,
        cell_label,
        cell_cls,
    ):
        if "total" in k.lower():
            return None
        if k.startswith("p_"):
            k = k[2:]
        col_dim_instance = cls._get_col_dim_instance(col_dim_cls, k)
        cell_instance = cell_cls.from_value(v)

        dim_idx = {}
        if time is not None:
            dim_idx["Time"] = time

        dim_idx[row_dim_cls.__name__] = row_dim_instance
        if col_dim_cls:
            dim_idx[col_dim_cls.__name__] = col_dim_instance

        return Datum(
            entity_cls,
            dim_idx,
            {cell_label: cell_instance},
        )

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
        row_dim_instance = cls._get_row_dim_instance(
            row_dim_cls, row_dim_key, d
        )
        if not row_dim_instance:
            return []

        datum_list = []
        for k, v in d["values"].items():
            datum = cls._get_datum_from_kv(
                k,
                v,
                entity_cls,
                time,
                row_dim_cls,
                row_dim_instance,
                col_dim_cls,
                cell_label,
                cell_cls,
            )
            if datum is not None:
                datum_list.append(datum)
        return datum_list
