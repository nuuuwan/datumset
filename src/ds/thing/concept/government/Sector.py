# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class Sector(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 0 - 4
            cls("Urban"),
            cls("Rural"),
            cls("Estate"),
            cls("EstateRural"),
            cls("EstateUrban"),
        ]
