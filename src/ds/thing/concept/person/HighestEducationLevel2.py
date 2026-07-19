# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel2(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("never_attended_school"),
            cls("studied_in_a_special_school_or_special_unit"),
            cls("passed_grade_1_5"),
            cls("passed_grade_6_8"),
            cls("passed_grade_9_10"),
            # 6 - 8
            cls("passed_gce_o_or_l"),
            cls("passed_gce_a_or_l"),
            cls("degree_or_above"),
        ]
