from ds.datum.Datum import Datum
from ds.thing.concept.atom.Float import Float


class DerivedQueryChangeMixin:

    @classmethod
    def _get_change_datums(cls, base_datumset, group_dims):
        target_dim = cls._get_target_dim_label(base_datumset)
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
