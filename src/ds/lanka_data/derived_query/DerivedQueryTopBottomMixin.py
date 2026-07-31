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

    @classmethod
    def _get_nth_datums(cls, base_datumset, group_dims, n):
        groups = {}
        for datum in base_datumset:
            key = cls._get_group_key(datum, group_dims)
            groups.setdefault(key, []).append(datum)
        result = []
        for datums in groups.values():
            sorted_d = sorted(datums, key=cls._get_count, reverse=True)
            if len(sorted_d) >= n:
                result.append(sorted_d[n - 1])
        return result

    @classmethod
    def _get_2nd_datums(cls, base_datumset, group_dims):
        return cls._get_nth_datums(base_datumset, group_dims, 2)

    @classmethod
    def _get_3rd_datums(cls, base_datumset, group_dims):
        return cls._get_nth_datums(base_datumset, group_dims, 3)
