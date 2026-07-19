# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class ResidentRelativeToDistrict(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 2
            cls("in_district"),
            cls("in_other_district"),
        ]
