# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupWorking(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 3
            cls("AgeBelow20"),
            cls("Age2064"),
            cls("Age65Above"),
        ]
