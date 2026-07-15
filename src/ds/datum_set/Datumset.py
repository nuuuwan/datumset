import json
from dataclasses import dataclass

from utils_future import Log

from ds.datum.Datum import Datum
from ds.query.Query import Query

log = Log('Datumset')


@dataclass(frozen=True)
class Datumset:
    _value: set[Datum]

    def __init__(self, *data: Datum):
        object.__setattr__(self, '_value', set(data))

    @property
    def first_datum(self):
        return next(iter(self._value))

    @staticmethod
    def _flatten_match_list(x_list):
        assert isinstance(x_list, list)
        first_item = x_list[0]
        if not isinstance(first_item, dict):
            return x_list
        final = {}
        for item in x_list:
            for k, v in item.items():
                final[k] = v
        return final

    def _flatten_all_matches(self, raw):
        return {
            k: self._flatten_match_list([json.loads(v_item) for v_item in v])
            for k, v in raw.items()
        }

    def _build_raw_matches(self, matches):
        raw = {}
        for match_items in matches:
            for k, v in json.loads(match_items).items():
                if k not in raw:
                    raw[k] = set()
                raw[k].add(json.dumps(v))
        return raw

    def _build_final_match(self, matches):
        return self._flatten_all_matches(self._build_raw_matches(matches))

    def _find_matches(self, query):
        matching_subset = set()
        matches = set()
        for datam in self._value:
            candidate_match = datam.is_match(query)
            if candidate_match:
                log.debug(f'{candidate_match=}')
                matching_subset.add(datam)
                matches.add(json.dumps(candidate_match))
        return matching_subset, matches

    def is_match(self, query: Query) -> bool:
        matching_subset, matches = self._find_matches(query)
        if not matching_subset:
            return False
        return Datumset(*matching_subset), self._build_final_match(matches)
