# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class NonCommunicableDisease(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("high_blood_pressure"),
            cls("diabetes"),
            cls("high_cholesterol"),
            cls("heart_disease"),
            cls("asthma"),
            # 6 - 10
            cls("kidney_disease"),
            cls("stroke_or_paralysis"),
            cls("cancer"),
            cls("epilepsy"),
            cls("thalassemia"),
        ]
