# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class SingleOrMultipleDisabilities(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 3
            cls("with_single_disability"),
            cls("with_more_than_one_disability"),
            cls("no_disability"),
        ]
