from ds.thing.concept.household.CookingFuel import CookingFuel
from ds.thing.concept.household.FloorType import FloorType
from ds.thing.concept.household.HouseholdAppliances import HouseholdAppliances
from ds.thing.concept.household.HouseholdOccupancy import HouseholdOccupancy
from ds.thing.concept.household.HouseholdSize import HouseholdSize
from ds.thing.concept.household.HouseholdStructure import HouseholdStructure
from ds.thing.concept.household.HouseholdType import HouseholdType
from ds.thing.concept.household.Lighting import Lighting
from ds.thing.concept.household.LiquidWasteDisposal import LiquidWasteDisposal
from ds.thing.concept.household.LivingQuarters import LivingQuarters
from ds.thing.concept.household.OccupationStatus import OccupationStatus
from ds.thing.concept.household.OneRoomOrMore import OneRoomOrMore
from ds.thing.concept.household.OwnershipStatus import OwnershipStatus
from ds.thing.concept.household.RoofType import RoofType
from ds.thing.concept.household.SolidWasteDisposal import SolidWasteDisposal
from ds.thing.concept.household.SourceOfDrinkingWater import SourceOfDrinkingWater
from ds.thing.concept.household.ToiletFacilities import ToiletFacilities
from ds.thing.concept.household.TypeOfUnit import TypeOfUnit
from ds.thing.concept.household.WallType import WallType
from ds.thing.concept.household.WaterSupplyAvailability import WaterSupplyAvailability


class EntityClassListHouseholdMixin:
    ENTITY_CLASS_LIST = [
        CookingFuel,
        FloorType,
        HouseholdAppliances,
        HouseholdOccupancy,
        HouseholdSize,
        #
        HouseholdStructure,
        HouseholdType,
        Lighting,
        LiquidWasteDisposal,
        LivingQuarters,
        #
        OccupationStatus,
        OneRoomOrMore,
        OwnershipStatus,
        RoofType,
        SolidWasteDisposal,
        #
        SourceOfDrinkingWater,
        ToiletFacilities,
        TypeOfUnit,
        WallType,
        WaterSupplyAvailability,
        #
    ]
