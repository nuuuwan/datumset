# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationReason(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 0 - 4
            cls("Marriage"),
            cls("EmploymentSearchingForJob"),
            cls("Education"),
            cls("AccompaniedAFamilyMember"),
            cls("ReturningForPermanentResidence"),
            # 5 - 8
            cls("DevelopmentProjects"),
            cls("ResettledAfterDisplacement"),
            cls("ADisasterADisplacedHappenedInThePriorPlace"),
            cls("Other"),
        ]
