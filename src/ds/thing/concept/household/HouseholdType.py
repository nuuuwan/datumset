# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 4
            cls("OnePerson"),
            cls("Nuclear"),
            cls("Extended"),
            cls("Composite"),
        ]
