from ds.datumset.DatumsetBase import DatumsetBase
from ds.datumset.DatumsetSerializeMixin import DatumsetSerializeMixin
from ds.datumset.DatumsetSplitMixin import DatumsetSplitMixin


class Datumset(
    DatumsetSerializeMixin,
    DatumsetBase,
    DatumsetSplitMixin,
):

    def dedupe(self):
        data = self.to_data()
        return Datumset.from_data(data)
