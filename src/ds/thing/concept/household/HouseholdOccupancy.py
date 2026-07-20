# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdOccupancy(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 2
            "occupied",
            "permanently_closed_or_vacant",
        ]
