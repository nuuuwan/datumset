from functools import cache

from ds.thing.concept.Ethnicity import Ethnicity
from ds.thing.concept.HighestEducationLevel import HighestEducationLevel
from ds.thing.concept.Int import Int
from ds.thing.concept.IsEconomicallyActive import IsEconomicallyActive
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.Religion import Religion
from ds.thing.concept.Time import Time
from ds.thing.entity.House import House
from ds.thing.entity.Person import Person


class ThingFactory:

    ENTITY_CLASS_LIST = [
        Religion,
        Ethnicity,
        Person,
        House,
        Int,
        Time,
        IsEconomicallyActive,
        HighestEducationLevel,
    ]
    ENTITY_CLASS_IDX = {cls.__name__: cls for cls in ENTITY_CLASS_LIST}

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
