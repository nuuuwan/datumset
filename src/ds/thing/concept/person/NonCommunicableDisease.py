# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class NonCommunicableDisease(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("HighBloodPressure"),
            cls("Diabetes"),
            cls("HighCholesterol"),
            cls("HeartDisease"),
            cls("Asthma"),
            # 6 - 10
            cls("KidneyDisease"),
            cls("StrokeOrParalysis"),
            cls("Cancer"),
            cls("Epilepsy"),
            cls("Thalassemia"),
        ]
