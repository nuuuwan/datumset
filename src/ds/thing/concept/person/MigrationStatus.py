# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 3
            "local",
            "foreign",
            "migrant",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "local": "#D05D38",
            "foreign": "#3840D0",
            "migrant": "#6CD038",
        }
