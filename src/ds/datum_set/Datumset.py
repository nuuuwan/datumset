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

    def sorted_values(self, query):
        entity_list = query.entity_list
        time_list = query.time_list

        entity_to_rank = {
            entity: rank for rank, entity in enumerate(entity_list)
        }
        time_to_rank = {time: rank for rank, time in enumerate(time_list)}

        return sorted(
            self._value,
            key=lambda datam: (
                entity_to_rank.get(datam.entity_class.__name__, float('inf')),
                time_to_rank.get(datam.time._value, float('inf')),
            ),
        )

    def _find_matches(self, query):
        matching_subset = []
        all_time = []
        all_entity = []
        all_measurement = {}
        for datam in self.sorted_values(query):
            candidate_match = datam.is_match(query)
            if candidate_match:
                matching_subset.append(datam)
                candidate_time = candidate_match['time']
                candidate_entity = candidate_match['entity']
                candidate_measurement = candidate_match['measurement']

                if candidate_time not in all_time:
                    all_time.append(candidate_time)
                if candidate_entity not in all_entity:
                    all_entity.append(candidate_entity)
                for k, v in candidate_measurement.items():
                    if k not in all_measurement:
                        all_measurement[k] = v

        return matching_subset, dict(
            time=all_time,
            entity=all_entity,
            measurement=all_measurement,
        )

    def is_match(self, query: Query) -> bool:
        matching_subset, matches = self._find_matches(query)
        if not matching_subset:
            return False
        return Datumset(*matching_subset), matches
