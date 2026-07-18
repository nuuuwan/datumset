# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationDirection(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 2
            cls("InMigrants"),
            cls("OutMigrants"),
        ]
