from utils_future import Log

from ds.thing.concept.region.Region import Region
from ds.thing.ThingFactory import ThingFactory

log = Log("StandardTableAdapterRowMixin")


class StandardTableAdapterRowMixin:

    @classmethod
    def _get_col_dim_instance(cls, col_dim_cls, k):
        if col_dim_cls:
            return (
                ThingFactory.from_kvpair(k)
                if ":" in k
                else col_dim_cls.from_value(k)
            )
        return None

    @classmethod
    def _safe_from_region_id(cls, row_dim_cls, row_value):
        try:
            return row_dim_cls.from_region_id(row_value)
        except ValueError:
            return None

    @classmethod
    def _safe_from_value(cls, row_dim_cls, row_value):
        try:
            return row_dim_cls.from_value(row_value)
        except ValueError as e:
            log.error(e)
            return None

    @classmethod
    def _get_row_dim_instance(cls, row_dim_cls, row_dim_key, d):
        row_value = d[row_dim_key]
        if row_dim_key == "region_id" and issubclass(row_dim_cls, Region):
            return cls._safe_from_region_id(row_dim_cls, row_value)
        return cls._safe_from_value(row_dim_cls, row_value)
