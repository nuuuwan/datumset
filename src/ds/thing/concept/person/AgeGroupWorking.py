# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupWorking(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 3
            "age_below_20",
            "age_20_64",
            "age_65_above",
        ]
