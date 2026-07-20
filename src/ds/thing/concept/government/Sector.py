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
