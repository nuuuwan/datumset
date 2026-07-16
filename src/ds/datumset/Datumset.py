from ds.datumset.DatumsetBase import DatumsetBase
from ds.datumset.DatumsetMatchMixin import DatumsetMatchMixin
from ds.datumset.DatumsetQueryMixin import DatumsetQueryMixin
from ds.datumset.DatumsetSerializeMixin import DatumsetSerializeMixin


class Datumset(
    DatumsetQueryMixin,
    DatumsetMatchMixin,
    DatumsetSerializeMixin,
    DatumsetBase,
):
    pass
