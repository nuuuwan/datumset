# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmmigrationReason(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 4
            "employment",
            "education",
            "accompanying_family_member_in_need",
            "other",
        ]
