from dataclasses import dataclass

from ds.datum.Datum import Datum
from ds.query.Query import Query
from utils_future import Log

log = Log('Datumset')


@dataclass(frozen=True)
class Datumset:
    _value: list[Datum]

    def __init__(self, *data: Datum):
        object.__setattr__(self, '_value', set(data))

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
            return False
        return Datumset(*matching_subset)

    def to_data(self):
        return [datum.to_data() for datum in self._value]

    @classmethod
    def from_data(cls, data):
        return cls(*[Datum.from_data(datum_data) for datum_data in data])
