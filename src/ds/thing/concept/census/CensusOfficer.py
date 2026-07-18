# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusOfficer(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("DeputyCensusCommissioners"),
            cls("AssistantCensusCommissioners"),
            cls("TechnicalStaffZonalSupervisorsAndDistrictStatisticalBranchHead"),
            cls("TechnicalStaffDivisionalCensusOfficer"),
            cls("TechnicalStaffAreaSupervisors"),
            # 6 - 9
            cls("TechnicalStaffCircleOfficers"),
            cls("OtherNonTechnicalStaff"),
            cls("EnumeratorsWhoUsedTabletComputersCapi"),
            cls("EnumeratorsWhoUsedSmartPhonesByoad"),
        ]
