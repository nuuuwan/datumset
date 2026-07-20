# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class SingleOrMultipleDisabilities(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 3
            "with_single_disability",
            "with_more_than_one_disability",
            "no_disability",
        ]
