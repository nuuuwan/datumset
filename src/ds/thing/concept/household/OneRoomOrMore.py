# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class OneRoomOrMore(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 2
            "with_only_one_room",
            "with_only_more_than_one_room",
        ]
