# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class OneRoomOrMore(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 2
            cls("WithOnlyOneRoom"),
            cls("WithOnlyMoreThanOneRoom"),
        ]
