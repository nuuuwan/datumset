# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdOccupancy(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 2
            cls("Occupied"),
            cls("PermanentlyClosedOrVacant"),
        ]
