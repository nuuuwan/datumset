from functools import cache

from ds.datumset.Datumset import Datumset
from ds.query.Query import Query


class LankaDataDerivedQueryMixin:

    CELL_TOP = "Top"
    CELL_COUNT = "Count"

    @classmethod
    def is_derived(cls, query_str):
        return Query(query_str).cell_part == cls.CELL_TOP

    @classmethod
    def _get_base_query_str(cls, query):
        return "/".join([query.entity_part, query.dim_part, cls.CELL_COUNT])

    @classmethod
    def _get_count(cls, datum):
        return float(datum.cell_idx[cls.CELL_COUNT].get_value())

    @classmethod
    def _get_group_key(cls, datum, group_dims):
        return tuple(datum.dim_idx[dim].get_value() for dim in group_dims)

    @classmethod
    def _get_top_datums(cls, base_datumset, group_dims):
        best = {}
        for datum in base_datumset:
            key = cls._get_group_key(datum, group_dims)
            count = cls._get_count(datum)
            if key not in best or count > best[key][1]:
                best[key] = (datum, count)
        return [datum for datum, _ in best.values()]

    @classmethod
    def _get_top_target_dim_label(cls, base_datumset):
        if len(base_datumset) == 0:
            return None
        return base_datumset[0].query.dim_labels[-1]

    @classmethod
    @cache
    def _get_derived(cls, query_str):
        query = Query(query_str)
        base_datumset = cls[cls._get_base_query_str(query)]
        target_dim_label = cls._get_top_target_dim_label(base_datumset)
        if target_dim_label is None:
            return Datumset.empty()
        group_dims = [
            dim_label
            for dim_label in query.dim_labels
            if dim_label != target_dim_label
        ]
        top_datums = cls._get_top_datums(base_datumset, group_dims)
        datumset = Datumset(*top_datums)
        object.__setattr__(datumset, "_query_str", query_str)
        return datumset
