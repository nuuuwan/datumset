class DerivedQueryCommonMixin:

    CELL_COUNT = "Count"

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
    def _get_target_dim_label(cls, base_datumset):
        if len(base_datumset) == 0:
            return None
        return base_datumset[0].query.dim_labels[-1]
