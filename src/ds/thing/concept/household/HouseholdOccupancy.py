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

    @classmethod
    def get_color_map(cls):
        return {
            "occupied": "#D05D38",
            "permanently_closed_or_vacant": "#3840D0",
        }
