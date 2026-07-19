# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationDirection(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 2
            cls("in_migrants"),
            cls("out_migrants"),
        ]
