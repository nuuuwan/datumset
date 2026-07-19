# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class OneRoomOrMore(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 2
            cls("with_only_one_room"),
            cls("with_only_more_than_one_room"),
        ]
