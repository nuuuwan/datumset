# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmmigrationReason(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 4
            cls("employment"),
            cls("education"),
            cls("accompanying_family_member_in_need"),
            cls("other"),
        ]
