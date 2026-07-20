# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class LanguageLiteracy(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 4
            "at_least_one_language",
            "sinhala",
            "tamil",
            "english",
        ]
