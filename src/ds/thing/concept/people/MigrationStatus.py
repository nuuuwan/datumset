# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 0 - 2
            cls("Local"),
            cls("Foreign"),
            cls("Migrant"),
        ]
