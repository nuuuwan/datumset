# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class ResidentRelativeToDistrict(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 2
            "in_district",
            "in_other_district",
        ]
