# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class LanguageLiteracy(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 4
            cls("AtLeastOneLanguage"),
            cls("Sinhala"),
            cls("Tamil"),
            cls("English"),
        ]
