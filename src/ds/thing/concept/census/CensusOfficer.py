# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusOfficer(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("DeputyCensusCommissioners"),
            cls("AssistantCensusCommissioners"),
            cls(
                "TechnicalStaffZonalSupervisorsAndDistrictStatisticalBranchHead"
            ),
            cls("TechnicalStaffDivisionalCensusOfficer"),
            cls("TechnicalStaffAreaSupervisors"),
            cls("TechnicalStaffCircleOfficers"),
            cls("OtherNonTechnicalStaff"),
            cls("EnumeratorsWhoUsedTabletComputersCapi"),
            cls("EnumeratorsWhoUsedSmartPhonesByoad"),
        ]
