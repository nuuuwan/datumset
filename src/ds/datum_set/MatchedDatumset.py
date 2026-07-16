import json
import os
from dataclasses import dataclass

from ds.datum_set.Datumset import Datumset
from ds.query.Query import Query
from utils_future import JSONFile, Log

log = Log("MatchedDatumset")


@dataclass(frozen=True)
class MatchedDatumset:
    query: Query
    datumset: Datumset

    def to_data(self):
        return dict(
            query=self.query.query_str,
            datumset=self.datumset.to_data(),
        )

    def to_str(self):
        return json.dumps(self.to_data(), indent=4)

    @classmethod
    def from_data(cls, data):
        return cls(
            query=Query(data["query"]),
            datumset=Datumset.from_data(data["datumset"]),
        )

    @classmethod
    def from_str(cls, data_str):
        return cls.from_data(json.loads(data_str))

    def to_file(self):
        os.makedirs("data", exist_ok=True)
        json_file = JSONFile(os.path.join("data", "ds.json"))
        json_file.write(self.to_data())
        log.info(f"Wrote {json_file}")
