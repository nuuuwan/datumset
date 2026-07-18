# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmmigrationReason(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 4
            cls("Employment"),
            cls("Education"),
            cls("AccompanyingFamilyMemberInNeed"),
            cls("Other"),
        ]
