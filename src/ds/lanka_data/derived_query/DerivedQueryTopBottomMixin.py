class DerivedQueryTopBottomMixin:

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
    def _get_bottom_datums(cls, base_datumset, group_dims):
        best = {}
        for datum in base_datumset:
            key = cls._get_group_key(datum, group_dims)
            count = cls._get_count(datum)
            if key not in best or count < best[key][1]:
                best[key] = (datum, count)
        return [datum for datum, _ in best.values()]
