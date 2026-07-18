# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupUnderAndOver18Years(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 2
            cls("Under18Years"),
            cls("18YearsAndOver"),
        ]
