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
        ]

    @classmethod
    def map_alias(cls):
        return {
            "stroke": "stroke_or_paralysis",
        }

    @classmethod
    def get_color_map(cls):
        return {
            "high_blood_pressure": "#D05D38",
            "diabetes": "#3840D0",
            "high_cholesterol": "#6CD038",
            "heart_disease": "#D03899",
            "asthma": "#38C5D0",
            "kidney_disease": "#D0AF38",
            "stroke_or_paralysis": "#8238D0",
            "cancer": "#38D056",
            "epilepsy": "#D03847",
            "thalassemia": "#3873D0",
        }
