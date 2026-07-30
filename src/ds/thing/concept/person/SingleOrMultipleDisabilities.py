# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class SingleOrMultipleDisabilities(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 3
            "with_single_disability",
            "with_more_than_one_disability",
            "no_disability",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "with_single_disability": "#D05D38",
            "with_more_than_one_disability": "#3840D0",
            "no_disability": "#cccccc",
        }
