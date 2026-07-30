# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class TimeGroup0510More(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 3
            "00_to_04_years",
            "05_to_09_years",
            "10_or_more_years",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "00_to_04_years": "#D05D38",
            "05_to_09_years": "#3840D0",
            "10_or_more_years": "#6CD038",
        }
