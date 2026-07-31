from ds.datum.Datum import Datum
from ds.thing.concept.atom.Float import Float
from ds.thing.concept.atom.Int import Int


class DerivedQueryRankShareMixin:

    @classmethod
    def _get_rank_datums(cls, base_datumset, group_dims):
        groups = {}
        for datum in base_datumset:
            key = cls._get_group_key(datum, group_dims)
            groups.setdefault(key, []).append(datum)
        result = []
        for datums in groups.values():
            sorted_d = sorted(datums, key=cls._get_count, reverse=True)
            for rank, datum in enumerate(sorted_d, 1):
                result.append(
                    Datum(
                        datum.entity_class,
                        datum.dim_idx,
                        {'Rank': Int.from_value(rank)},
                    )
                )
        return result

    @classmethod
    def _get_share_datums(cls, base_datumset, group_dims):
        groups = {}
        for datum in base_datumset:
            key = cls._get_group_key(datum, group_dims)
            groups.setdefault(key, []).append(datum)
        result = []
        for datums in groups.values():
            total = sum(cls._get_count(d) for d in datums)
            for datum in datums:
                share = cls._get_count(datum) / total if total else 0.0
                result.append(
                    Datum(
                        datum.entity_class,
                        datum.dim_idx,
                        {'Share': Float.from_value(share)},
                    )
                )
        return result
