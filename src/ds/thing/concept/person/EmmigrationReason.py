# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmmigrationReason(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 4
            "employment",
            "education",
            "accompanying_family_member_in_need",
            "other",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "employment": "#D05D38",
            "education": "#3840D0",
            "accompanying_family_member_in_need": "#6CD038",
            "other": "#cccccc",
        }
