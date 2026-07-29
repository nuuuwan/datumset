from ds.thing.concept.person.AgeGroup import AgeGroup
from ds.thing.concept.person.AgeGroupWorking import AgeGroupWorking
from ds.thing.concept.person.DisabilityTypes import DisabilityTypes
from ds.thing.concept.person.EconomicInactivityReason import \
    EconomicInactivityReason
from ds.thing.concept.person.EducationActivity import EducationActivity
from ds.thing.concept.person.EmmigrationReason import EmmigrationReason
from ds.thing.concept.person.EmploymentStatus import EmploymentStatus
from ds.thing.concept.person.Ethnicity import Ethnicity
from ds.thing.concept.person.Gender import Gender
from ds.thing.concept.person.HighestEducationLevel import HighestEducationLevel
from ds.thing.concept.person.HighestEducationLevel2 import \
    HighestEducationLevel2
from ds.thing.concept.person.HighestEducationLevel3 import \
    HighestEducationLevel3
from ds.thing.concept.person.IsEconomicallyActive import IsEconomicallyActive
from ds.thing.concept.person.LanguageLiteracy import LanguageLiteracy
from ds.thing.concept.person.LiveBirths import LiveBirths
from ds.thing.concept.person.MaritalStatus import MaritalStatus
from ds.thing.concept.person.MigrationDirection import MigrationDirection
from ds.thing.concept.person.MigrationReason import MigrationReason
from ds.thing.concept.person.MigrationStatus import MigrationStatus
from ds.thing.concept.person.NonCommunicableDisease import \
    NonCommunicableDisease
from ds.thing.concept.person.Religion import Religion
from ds.thing.concept.person.ResidentRelativeToDistrict import \
    ResidentRelativeToDistrict
from ds.thing.concept.person.Sex import Sex
from ds.thing.concept.person.SingleOrMultipleDisabilities import \
    SingleOrMultipleDisabilities


class EntityClassListPersonMixin:
    ENTITY_CLASS_LIST = [
        AgeGroup,
        AgeGroupWorking,
        DisabilityTypes,
        EconomicInactivityReason,
        EducationActivity,
        #
        EmmigrationReason,
        EmploymentStatus,
        Ethnicity,
        Gender,
        HighestEducationLevel,
        #
        HighestEducationLevel2,
        HighestEducationLevel3,
        IsEconomicallyActive,
        LanguageLiteracy,
        LiveBirths,
        #
        MaritalStatus,
        MigrationDirection,
        MigrationReason,
        MigrationStatus,
        NonCommunicableDisease,
        #
        Religion,
        ResidentRelativeToDistrict,
        Sex,
        SingleOrMultipleDisabilities,
    ]
