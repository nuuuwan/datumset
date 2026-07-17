from functools import cache

from ds.thing.concept.AgeGroup import AgeGroup
from ds.thing.concept.CookingFuel import CookingFuel
from ds.thing.concept.Ethnicity import Ethnicity
from ds.thing.concept.FloorType import FloorType
from ds.thing.concept.Gender import Gender
from ds.thing.concept.HighestEducationLevel import HighestEducationLevel
from ds.thing.concept.HouseholdStructure import HouseholdStructure
from ds.thing.concept.Int import Int
from ds.thing.concept.IsEconomicallyActive import IsEconomicallyActive
from ds.thing.concept.Lighting import Lighting
from ds.thing.concept.LivingQuarters import LivingQuarters
from ds.thing.concept.MaritalStatus import MaritalStatus
from ds.thing.concept.OccupationStatus import OccupationStatus
from ds.thing.concept.OwnershipStatus import OwnershipStatus
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.Religion import Religion
from ds.thing.concept.RoofType import RoofType
from ds.thing.concept.SolidWasteDisposal import SolidWasteDisposal
from ds.thing.concept.SourceOfDrinkingWater import SourceOfDrinkingWater
from ds.thing.concept.Time import Time
from ds.thing.concept.ToiletFacilities import ToiletFacilities
from ds.thing.concept.TypeOfUnit import TypeOfUnit
from ds.thing.concept.WallType import WallType
from ds.thing.entity.House import House
from ds.thing.entity.Person import Person


class ThingFactory:

    ENTITY_CLASS_LIST = [
        AgeGroup,
        CookingFuel,
        Ethnicity,
        FloorType,
        Gender,
        HighestEducationLevel,
        House,
        HouseholdStructure,
        Int,
        IsEconomicallyActive,
        Lighting,
        LivingQuarters,
        MaritalStatus,
        OccupationStatus,
        OwnershipStatus,
        Person,
        Religion,
        RoofType,
        SolidWasteDisposal,
        SourceOfDrinkingWater,
        Time,
        ToiletFacilities,
        TypeOfUnit,
        WallType,
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
