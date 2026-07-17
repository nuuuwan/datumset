from ds.datum.DatumBase import DatumBase
from ds.datum.DatumMatchMixin import DatumMatchMixin
from ds.datum.DatumQueryMixin import DatumQueryMixin
from ds.datum.DatumSerializeMixin import DatumSerializeMixin


class Datum(DatumMatchMixin, DatumSerializeMixin, DatumQueryMixin, DatumBase):
    pass
