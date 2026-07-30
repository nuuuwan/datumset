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
    @cache
    def _get_derived(cls, query_str):
        query = Query(query_str)
        base_datumset = cls[cls._get_base_query_str(query)]
        group_dims = query.dim_labels[:-1]
        top_datums = cls._get_top_datums(base_datumset, group_dims)
        datumset = Datumset(_top_datums)
        object.__setattr__(datumset, "_query_str", query_str)
        return datumset
