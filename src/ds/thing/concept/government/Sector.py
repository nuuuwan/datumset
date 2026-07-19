# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class Sector(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("urban"),
            cls("rural"),
            cls("estate"),
            cls("estate_rural"),
            cls("estate_urban"),
        ]
