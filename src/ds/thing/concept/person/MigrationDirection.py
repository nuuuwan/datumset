# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationDirection(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 2
            "in_migrants",
            "out_migrants",
        ]
