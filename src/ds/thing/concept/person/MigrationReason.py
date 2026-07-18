# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationReason(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("Marriage"),
            cls("EmploymentSearchingForJob"),
            cls("Education"),
            cls("AccompaniedAFamilyMember"),
            cls("ReturningForPermanentResidence"),
            # 6 - 9
            cls("DevelopmentProjects"),
            cls("ResettledAfterDisplacement"),
            cls("ADisasterADisplacedHappenedInThePriorPlace"),
            cls("Other"),
        ]
