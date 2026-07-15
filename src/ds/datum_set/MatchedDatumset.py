import json
from dataclasses import dataclass

from ds.datum_set.Datumset import Datumset
from ds.query.Query import Query


@dataclass(frozen=True)
class MatchedDatumset:
    query: Query
    datumset: Datumset

    def to_data(self):
        return dict(
            query=self.query.to_data(),
            datumset=self.datumset.to_data(),
        )

    def to_str(self):
        return json.dumps(self.to_data(), indent=4)

    @classmethod
    def from_data(cls, data):
        return cls(
            query=Query.from_data(data['query']),
            datumset=Datumset.from_data(data['datumset']),
        )

    @classmethod
    def from_str(cls, data_str):
        return cls.from_data(json.loads(data_str))
