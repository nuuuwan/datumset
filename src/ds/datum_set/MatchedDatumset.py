import json
from dataclasses import dataclass
from functools import cached_property

from ds.datum_set.Datumset import Datumset
from ds.query.Query import Query
from utils_future import Directory, JSONFile, Log

log = Log("MatchedDatumset")


@dataclass(frozen=True)
class MatchedDatumset:
    query: Query
    datumset: Datumset

    @cached_property
    def dir_data(self):
        dir_data = Directory("data", self.query.query_str)
        dir_data.make()
        return dir_data

    @cached_property
    def data_file(self):
        return JSONFile(self.dir_data.path, "data.json")

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
        self.data_file.write(self.to_data())
        log.info(f"Wrote {self.data_file}")
