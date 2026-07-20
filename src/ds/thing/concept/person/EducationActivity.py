# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EducationActivity(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "preschool_education",
            "school_education",
            "degree_or_postgraduate_education",
            "vocational_training_or_technical_education",
            "other_educational_activity",
            # 6 - 6
            "not_studying",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "pre_school": "preschool_education",
            "undergraduate_or_postgraduate_education": "degree_or_postgraduate_education",  # noqa: E501
        }
