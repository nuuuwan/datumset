# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AdministrativeEntity(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("assistant_government_agend_divisions"),
            cls("grama_sevaka_divisions"),
            cls("municipal_councils"),
            cls("urban_councils"),
            cls("town_councils"),
        ]
