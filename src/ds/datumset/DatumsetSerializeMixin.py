import json

from propcache import cached_property

from ds.datum.Datum import Datum
from utils_future import Directory, JSONFile, Log, ShallowDict

log = Log("DatumsetSerializeMixin")


class DatumsetSerializeMixin:
    @cached_property
    def dir_data(self):
        dir_data = Directory("data", self.query.query_str)
        dir_data.make()
        return dir_data

    @cached_property
    def data_file(self):
        return JSONFile(self.dir_data.path, "data.json")

    def to_data(self):
        shallow_d = ShallowDict()
        for datum in self._value:
            deep_d = datum.to_data()
            shallow_d_for_datum = ShallowDict.from_deep(deep_d)
            shallow_d += shallow_d_for_datum
        return shallow_d.to_deep()

    @classmethod
    def from_data(cls, data):
        shallow_d = ShallowDict.from_deep(data)
        datum_list = []
        for key_tuple, _ in shallow_d.items():
            shallow_d_for_datum = ShallowDict({key_tuple: 1})
            deep_d_for_datum = shallow_d_for_datum.to_deep()
            datum = Datum.from_data(deep_d_for_datum)
            datum_list.append(datum)
        return cls(*datum_list)

    def to_file(self):
        self.data_file.write(self.to_data())
        log.info(f"Wrote {self.data_file}")

    def to_str(self):
        return json.dumps(self.to_data(), indent=4)

    @classmethod
    def from_str(cls, data_str):
        data = json.loads(data_str)
        return cls.from_data(data)

    def __eq__(self, other):
        return self.to_data() == other.to_data()
