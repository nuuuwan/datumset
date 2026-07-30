from functools import cache

from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdSize(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7_or_more",
        ]

    @classmethod
    def map_alias(cls) -> dict:
        return {
            "7_or_over": "7_or_more",
        }

    @classmethod
    @cache
    def is_ordered(cls):
        return True
