from ds.datum.DatumBase import DatumBase
from ds.datum.DatumMatchMixin import DatumMatchMixin
from ds.datum.DatumSerializeMixin import DatumSerializeMixin


class Datum(DatumMatchMixin, DatumSerializeMixin, DatumBase):
    pass
