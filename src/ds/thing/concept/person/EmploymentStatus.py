# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmploymentStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("GovernmentOrSemiGovernmentPaidEmployee"),
            cls("PrivateSectorPaidEmployee"),
            cls("Employer"),
            cls("OwnAccountWorker"),
            cls("ContributingToFamilyEnterprise"),
        ]
