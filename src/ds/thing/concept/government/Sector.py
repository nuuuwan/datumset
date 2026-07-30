# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class Sector(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "urban",
            "rural",
            "estate",
            "estate_rural",
            "estate_urban",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "urban": "#D05D38",
            "rural": "#3840D0",
            "estate": "#6CD038",
            "estate_rural": "#D03899",
            "estate_urban": "#38C5D0",
        }
