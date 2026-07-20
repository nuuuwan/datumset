# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel2(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "never_attended_school",
            "studied_in_a_special_school_or_special_unit",
            "passed_grade_1_5",
            "passed_grade_6_8",
            "passed_grade_9_10",
            # 6 - 8
            "passed_gce_o_or_l",
            "passed_gce_a_or_l",
            "degree_or_above",
        ]
