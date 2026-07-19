# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class TimeGroup0510More(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 3
            cls("00_to_04_years"),
            cls("05_to_09_years"),
            cls("10_or_more_years"),
        ]
