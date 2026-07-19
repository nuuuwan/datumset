# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class LanguageLiteracy(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 4
            cls("at_least_one_language"),
            cls("sinhala"),
            cls("tamil"),
            cls("english"),
        ]
