from ds.query.Query import Query


class DatumsetMatchMixin:
    def _find_matches(self, query):
        matching_subset = []
        for datam in self._value:
            candidate_match = datam.is_match(query)
            if candidate_match:
                matching_subset.append(datam)

        return matching_subset

    def is_match(self, query: Query) -> bool:
        matching_subset = self._find_matches(query)
        if not matching_subset:
            return None
        return self.__class__(*matching_subset)
