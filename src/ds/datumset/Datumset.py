from ds.datumset.DatumsetBase import DatumsetBase
from ds.datumset.DatumsetMatchMixin import DatumsetMatchMixin
from ds.datumset.DatumsetSerializeMixin import DatumsetSerializeMixin


class Datumset(
    DatumsetMatchMixin,
    DatumsetSerializeMixin,
    DatumsetBase,
):
    pass
