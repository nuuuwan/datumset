from ds.query.Query import Query


class DatumsetMatchMixin:
    def _find_matching_datum_sublist(self, query):
        matching_datum_sublist = []
        for datam in self._value:
            if datam.is_match(query):
                matching_datum_sublist.append(datam)
        return matching_datum_sublist

    def is_match(self, query: Query) -> bool:
        matching_subset = self._find_matching_datum_sublist(query)
        if not matching_subset:
            return None
        return self.__class__(*matching_subset)
