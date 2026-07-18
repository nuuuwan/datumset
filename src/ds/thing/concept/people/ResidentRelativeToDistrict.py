# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class ResidentRelativeToDistrict(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 0 - 1
            cls("InDistrict"),
            cls("InOtherDistrict"),
        ]
