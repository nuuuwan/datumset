# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupCustom(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 4
            cls("LessThan18"),
            cls("18To29"),
            cls("30To59"),
            cls("60AndOver"),
        ]
