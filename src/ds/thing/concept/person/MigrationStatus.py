# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 3
            "local",
            "foreign",
            "migrant",
        ]
