from functools import cache

from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.ThingFactoryEntityClassListMixin import (
    ThingFactoryEntityClassListMixin,
)


class ThingFactory(ThingFactoryEntityClassListMixin):

    ENTITY_CLASS_IDX = {
        cls.__name__: cls
        for cls in ThingFactoryEntityClassListMixin.ENTITY_CLASS_LIST
    }

    @classmethod
    @cache
    def __class_getitem__(cls, class_name: str):

        try:
            region_entity_class = RegionFactory[class_name]
            return region_entity_class
        except ValueError:
            pass

        if class_name in cls.ENTITY_CLASS_IDX:
            return cls.ENTITY_CLASS_IDX[class_name]

        raise ValueError(f"[ThingFactory] Unknown class_name: {class_name}")

    @classmethod
    @cache
    def from_kvpair(cls, kvpair):
        class_name, value = kvpair.split(":")
        cls_for_name = ThingFactory[class_name]
        inst = cls_for_name.from_value(value)
        return inst
