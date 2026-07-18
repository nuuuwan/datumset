from ds.thing.concept.election.ElectionType import ElectionType
from ds.thing.concept.election.Party import Party
from ds.thing.concept.election.Summary import Summary
from ds.thing.concept.household.CookingFuel import CookingFuel
from ds.thing.concept.household.FloorType import FloorType
from ds.thing.concept.household.HouseholdStructure import HouseholdStructure
from ds.thing.concept.household.Lighting import Lighting
from ds.thing.concept.household.LivingQuarters import LivingQuarters
from ds.thing.concept.household.OccupationStatus import OccupationStatus
from ds.thing.concept.household.OwnershipStatus import OwnershipStatus
from ds.thing.concept.household.RoofType import RoofType
from ds.thing.concept.household.SolidWasteDisposal import SolidWasteDisposal
from ds.thing.concept.household.SourceOfDrinkingWater import (
    SourceOfDrinkingWater,
)
from ds.thing.concept.household.ToiletFacilities import ToiletFacilities
from ds.thing.concept.household.TypeOfUnit import TypeOfUnit
from ds.thing.concept.household.WallType import WallType
from ds.thing.concept.Int import Int
from ds.thing.concept.person.AgeGroup import AgeGroup
from ds.thing.concept.person.Ethnicity import Ethnicity
from ds.thing.concept.person.Gender import Gender
from ds.thing.concept.person.HighestEducationLevel import HighestEducationLevel
from ds.thing.concept.person.IsEconomicallyActive import IsEconomicallyActive
from ds.thing.concept.person.MaritalStatus import MaritalStatus
from ds.thing.concept.person.Religion import Religion
from ds.thing.concept.Time import Time
from ds.thing.entity.House import House
from ds.thing.entity.Person import Person
from ds.thing.entity.Vote import Vote


class ThingFactoryEntityClassListMixin:
    ENTITY_CLASS_LIST = [
        AgeGroup,
        CookingFuel,
        ElectionType,
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
        Party,
        Person,
        Religion,
        RoofType,
        SolidWasteDisposal,
        SourceOfDrinkingWater,
        Summary,
        Time,
        ToiletFacilities,
        TypeOfUnit,
        Vote,
        WallType,
    ]
