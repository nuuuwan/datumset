# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class TimeGroup0510More(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 3
            cls("00To04Years"),
            cls("05To09Years"),
            cls("10OrMoreYears"),
        ]
