from dataclasses import dataclass

from ds.datum.Datum import Datum
from ds.query.Query import Query
from utils_future import Log

log = Log("Datumset")


@dataclass(frozen=True)
class Datumset:
    _value: list[Datum]

    def __init__(self, *data: Datum):
        object.__setattr__(self, "_value", set(data))

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
        arr = [datum.to_data() for datum in self._value]
        idx = {}
        for data in arr:
            entity_class_name = list(data.keys())[0]
            entity_data = data[entity_class_name]
            time_value = list(entity_data.keys())[0]
            time_data = entity_data[time_value]

            if entity_class_name not in idx:
                idx[entity_class_name] = {}
            if time_value not in idx[entity_class_name]:
                idx[entity_class_name][time_value] = []
            idx[entity_class_name][time_value].append(time_data)

        sorted_idx = {}
        for entity_class_name, entity_data in idx.items():
            sorted_idx[entity_class_name] = dict(
                sorted(entity_data.items(), key=lambda x: x[0])
            )
        sorted_sorted_idx = dict(
            sorted(sorted_idx.items(), key=lambda x: x[0])
        )

        return sorted_sorted_idx

    @classmethod
    def from_data(cls, data):
        datum_list = []
        for entity_class_name, entity_data in data.items():
            for time_value, time_data in entity_data.items():
                for time_data_item in time_data:
                    datum = Datum.from_attributes(
                        entity_class_name, time_value, time_data_item
                    )
                    datum_list.append(datum)

        return cls(*datum_list)
