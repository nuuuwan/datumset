# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class ResidentRelativeToDistrict(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 2
            "in_district",
            "in_other_district",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "in_district": "#D05D38",
            "in_other_district": "#3840D0",
        }
