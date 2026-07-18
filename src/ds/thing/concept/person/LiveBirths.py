# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class LiveBirths(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("0"),
            cls("1"),
            cls("2"),
            cls("3"),
            cls("4"),
            # 6 - 8
            cls("5"),
            cls("6"),
            cls("7OrMore"),
        ]
