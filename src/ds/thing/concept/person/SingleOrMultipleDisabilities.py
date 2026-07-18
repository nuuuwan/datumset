# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class SingleOrMultipleDisabilities(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 3
            cls("WithSingleDisability"),
            cls("WithMoreThanOneDisability"),
            cls("NoDisability"),
        ]
