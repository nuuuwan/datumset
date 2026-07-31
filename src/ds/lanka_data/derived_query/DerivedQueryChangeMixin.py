from ds.datum.Datum import Datum
from ds.thing.concept.atom.Float import Float


class DerivedQueryChangeMixin:

    @classmethod
    def _infer_target_dim(cls, base_datumset, group_dims):
        if len(base_datumset) == 0:
            return None
        group_dims_set = set(group_dims)
        candidates = [
            d
            for d in base_datumset[0].dim_idx.keys()
            if d not in group_dims_set
        ]
        return candidates[0] if candidates else None

    @classmethod
    def _get_change_datums(cls, base_datumset, group_dims):
        target_dim = cls._infer_target_dim(base_datumset, group_dims)
        if target_dim is None:
            return []
        groups = {}
        for datum in base_datumset:
            key = cls._get_group_key(datum, group_dims)
            groups.setdefault(key, []).append(datum)
        result = []
        for datums in groups.values():
            sorted_d = sorted(
                datums,
                key=lambda d: d.dim_idx[target_dim].get_value(),
            )
            if len(sorted_d) < 2:
                continue
            change = cls._get_count(sorted_d[-1]) - cls._get_count(
                sorted_d[0]
            )
            result.append(
                Datum(
                    sorted_d[-1].entity_class,
                    sorted_d[-1].dim_idx,
                    {'Change': Float.from_value(change)},
                )
            )
        return result
