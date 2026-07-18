# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class TimeGroup0510More(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 0 - 2
            cls("0004Years"),
            cls("0509Years"),
            cls("10OrMoreYears"),
        ]
