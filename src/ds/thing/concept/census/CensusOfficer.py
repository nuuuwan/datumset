# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusOfficer(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 0 - 4
            cls("DeputyCensusCommissioners"),
            cls("AssistantCensusCommissioners"),
            cls("TechnicalStaffZonalSupervisorsAndDistrictStatisticalBranchHead"),
            cls("TechnicalStaffDivisionalCensusOfficer"),
            cls("TechnicalStaffAreaSupervisors"),
            # 5 - 8
            cls("TechnicalStaffCircleOfficers"),
            cls("OtherNonTechnicalStaff"),
            cls("EnumeratorsWhoUsedTabletComputersCapi"),
            cls("EnumeratorsWhoUsedSmartPhonesByoad"),
        ]
