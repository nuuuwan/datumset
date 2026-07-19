# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 3
            cls("local"),
            cls("foreign"),
            cls("migrant"),
        ]
