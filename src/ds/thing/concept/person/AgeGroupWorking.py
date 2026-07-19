# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupWorking(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 3
            cls("age_below_20"),
            cls("age_20_64"),
            cls("age_65_above"),
        ]
