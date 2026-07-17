from functools import cache

from ds.datumset.Datumset import Datumset
from ds.lanka_data.LankaDataDBMixin import LankaDataDBMixin


class LankaData(LankaDataDBMixin):

    @classmethod
    @cache
    def __class_getitem__(cls, query_str):
        idx = cls.idx()
        datum_list = idx.get(query_str)
        if datum_list is not None:
            return Datumset(*datum_list)

        raise ValueError(
            f'No matching Datumset found for label: "{query_str}"'
        )
