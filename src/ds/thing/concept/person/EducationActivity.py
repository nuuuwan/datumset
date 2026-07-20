# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EducationActivity(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("preschool_education"),
            cls("school_education"),
            cls("degree_or_postgraduate_education"),
            cls("vocational_training_or_technical_education"),
            cls("other_educational_activity"),
            # 6 - 6
            cls("not_studying"),
        ]

    @classmethod
    def map_alias(cls):
        return {
            "pre_school": "preschool_education",
            "undergraduate_or_postgraduate_education": "degree_or_postgraduate_education",
        }
