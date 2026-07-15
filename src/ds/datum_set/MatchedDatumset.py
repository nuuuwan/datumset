import json
from dataclasses import dataclass

from ds.datum_set.Datumset import Datumset
from ds.query.Query import Query


@dataclass(frozen=True)
class MatchedDatumset:
    query: Query
    datumset: Datumset
    match: dict

    def to_data(self):
        idx = {}
        idx_inner = {}
        for datum in self.datumset._value:
            entity_class = datum.entity_class.__name__
            time = datum.time._value
            idx_inner = datum.to_data_inner(
                idx_inner, self.query.measurement_part
            )
            if entity_class not in idx:
                idx[entity_class] = {}
            if time not in idx[entity_class]:
                idx[entity_class][time] = []
            idx[entity_class][time] = idx_inner

        return dict(
            metadata=self.match,
            data=idx,
        )

    def to_str(self):
        return json.dumps(self.to_data(), indent=4)
