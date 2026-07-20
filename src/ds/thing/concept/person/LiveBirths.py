# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class LiveBirths(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "0",
            "1",
            "2",
            "3",
            "4",
            # 6 - 8
            "5",
            "6",
            "7_or_more",
        ]

    @classmethod
    def map_alias(cls) -> dict:
        return {
            "7_plus": "7_or_more",
        }
