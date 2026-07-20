# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 4
            "one_person",
            "nuclear",
            "extended",
            "composite",
        ]
