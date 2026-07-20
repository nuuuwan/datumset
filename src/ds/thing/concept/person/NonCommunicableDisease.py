# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class NonCommunicableDisease(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "high_blood_pressure",
            "diabetes",
            "high_cholesterol",
            "heart_disease",
            "asthma",
            # 6 - 10
            "kidney_disease",
            "stroke_or_paralysis",
            "cancer",
            "epilepsy",
            "thalassemia",
            # new
            "stroke",
        ]
