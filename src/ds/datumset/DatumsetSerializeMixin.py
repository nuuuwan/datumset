from propcache import cached_property

from ds.datum.Datum import Datum
from utils_future import Directory, JSONFile, Log, ShallowDict

log = Log("DatumsetSerializeMixin")


class DatumsetSerializeMixin:

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
        datum_cells = {}
        for key_tuple, value in shallow_d.items():
            datum_key = key_tuple[:-1]
            datum_cells.setdefault(datum_key, {})[key_tuple[-1]] = value
        datum_list = []
        for datum_key, cells in datum_cells.items():
            sd = ShallowDict({datum_key: cells})
            datum = Datum.from_data(sd.to_deep())
            datum_list.append(datum)
        return cls(*datum_list)

    def __eq__(self, other):
        return self.to_data() == other.to_data()
