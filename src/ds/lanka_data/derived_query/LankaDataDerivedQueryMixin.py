from functools import cache

from ds.datumset.Datumset import Datumset
from ds.lanka_data.derived_query.DerivedQueryChangeMixin import \
    DerivedQueryChangeMixin
from ds.lanka_data.derived_query.DerivedQueryCommonMixin import \
    DerivedQueryCommonMixin
from ds.lanka_data.derived_query.DerivedQueryRankShareMixin import \
    DerivedQueryRankShareMixin
from ds.lanka_data.derived_query.DerivedQueryTopBottomMixin import \
    DerivedQueryTopBottomMixin
from ds.query.Query import Query


class LankaDataDerivedQueryMixin(
    DerivedQueryTopBottomMixin,
    DerivedQueryRankShareMixin,
    DerivedQueryChangeMixin,
    DerivedQueryCommonMixin,
):
    CELL_TOP = "Top"
    CELL_2ND = "2nd"
    CELL_3RD = "3rd"
    CELL_BOTTOM = "Bottom"
    CELL_RANK = "Rank"
    CELL_SHARE = "Share"
    CELL_CHANGE = "Change"

    DERIVED_CELLS = {
        CELL_TOP,
        CELL_2ND,
        CELL_3RD,
        CELL_BOTTOM,
        CELL_RANK,
        CELL_SHARE,
        CELL_CHANGE,
    }

    @classmethod
    def is_derived(cls, query_str):
        return Query(query_str).cell_part in cls.DERIVED_CELLS

    @classmethod
    def _get_target_dim_for_cell(cls, query, base_datumset):
        if query.cell_part == cls.CELL_CHANGE:
            return query.dim_labels[-1]
        return cls._get_target_dim_label(base_datumset)

    @classmethod
    @cache
    def _get_derived(cls, query_str):
        query = Query(query_str)
        base_datumset = cls[cls._get_base_query_str(query)]
        target_dim_label = cls._get_target_dim_for_cell(query, base_datumset)
        if target_dim_label is None:
            return Datumset.empty()
        group_dims = [
            dim_label
            for dim_label in query.dim_labels
            if dim_label != target_dim_label
        ]
        handlers = {
            cls.CELL_TOP: cls._get_top_datums,
            cls.CELL_2ND: cls._get_2nd_datums,
            cls.CELL_3RD: cls._get_3rd_datums,
            cls.CELL_BOTTOM: cls._get_bottom_datums,
            cls.CELL_RANK: cls._get_rank_datums,
            cls.CELL_SHARE: cls._get_share_datums,
            cls.CELL_CHANGE: cls._get_change_datums,
        }
        datums = handlers[query.cell_part](base_datumset, group_dims)
        datumset = Datumset(*datums)
        object.__setattr__(datumset, "_query_str", query_str)
        return datumset
