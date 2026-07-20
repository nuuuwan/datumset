# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AdministrativeEntity(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "assistant_government_agend_divisions",
            "grama_sevaka_divisions",
            "municipal_councils",
            "urban_councils",
            "town_councils",
        ]
