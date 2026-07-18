from ds.thing.concept.person.AgeGroup import AgeGroup
from ds.thing.concept.Bool import Bool
from ds.thing.entity.Census import Census
from ds.thing.concept.census.CensusOfficer import CensusOfficer
from ds.thing.concept.census.CensusTopic import CensusTopic
from ds.thing.concept.household.CookingFuel import CookingFuel
from ds.thing.concept.region.Country import Country
from ds.thing.concept.region.DSD import DSD
from ds.thing.concept.region.District import District
from ds.thing.concept.region.ED import ED
from ds.thing.concept.election.ElectionType import ElectionType
from ds.thing.concept.person.Ethnicity import Ethnicity
from ds.thing.concept.household.FloorType import FloorType
from ds.thing.concept.region.GND import GND
from ds.thing.concept.person.Gender import Gender
from ds.thing.concept.person.HighestEducationLevel import HighestEducationLevel
from ds.thing.entity.House import House
from ds.thing.concept.household.HouseholdStructure import HouseholdStructure
from ds.thing.concept.Int import Int
from ds.thing.concept.person.IsEconomicallyActive import IsEconomicallyActive
from ds.thing.concept.region.LG import LG
from ds.thing.concept.household.Lighting import Lighting
from ds.thing.concept.household.LivingQuarters import LivingQuarters
from ds.thing.concept.person.MaritalStatus import MaritalStatus
from ds.thing.concept.household.OccupationStatus import OccupationStatus
from ds.thing.concept.household.OwnershipStatus import OwnershipStatus
from ds.thing.concept.region.PD import PD
from ds.thing.concept.election.Party import Party
from ds.thing.entity.Person import Person
from ds.thing.concept.region.Province import Province
from ds.thing.concept.person.Religion import Religion
from ds.thing.concept.household.RoofType import RoofType
from ds.thing.concept.person.Sex import Sex
from ds.thing.concept.household.SolidWasteDisposal import SolidWasteDisposal
from ds.thing.concept.household.SourceOfDrinkingWater import SourceOfDrinkingWater
from ds.thing.concept.election.Summary import Summary
from ds.thing.concept.Time import Time
from ds.thing.concept.household.ToiletFacilities import ToiletFacilities
from ds.thing.concept.household.TypeOfUnit import TypeOfUnit
from ds.thing.entity.Vote import Vote
from ds.thing.concept.household.WallType import WallType


class ThingFactoryEntityClassListMixin:
    ENTITY_CLASS_LIST = [
        # --------------------
        # census (2)
        # --------------------
        CensusOfficer,
        CensusTopic,
        # --------------------
        # concept (3)
        # --------------------
        Bool,
        Int,
        Time,
        # --------------------
        # election (3)
        # --------------------
        ElectionType,
        Party,
        Summary,
        # --------------------
        # entity (4)
        # --------------------
        Census,
        House,
        Person,
        Vote,
        # --------------------
        # household (13)
        # --------------------
        CookingFuel,
        FloorType,
        HouseholdStructure,
        Lighting,
        LivingQuarters,
        #
        OccupationStatus,
        OwnershipStatus,
        RoofType,
        SolidWasteDisposal,
        SourceOfDrinkingWater,
        #
        ToiletFacilities,
        TypeOfUnit,
        WallType,
        # --------------------
        # person (8)
        # --------------------
        AgeGroup,
        Ethnicity,
        Gender,
        HighestEducationLevel,
        IsEconomicallyActive,
        #
        MaritalStatus,
        Religion,
        Sex,
        # --------------------
        # region (8)
        # --------------------
        Country,
        DSD,
        District,
        ED,
        GND,
        #
        LG,
        PD,
        Province,
    ]
