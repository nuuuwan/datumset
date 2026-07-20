from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("primary"),
            cls("secondary"),
            cls("gce_ordinary_level"),
            cls("gce_advanced_level"),
            cls("degree_and_above"),
            cls("no_schooling"),
            #
            cls("never_attended_school"),
            cls("passed_grade_1_5"),
            cls("passed_grade_6_8"),
            cls("passed_grade_9_10"),
            cls("g_c_e_o_or_l_or_equal"),
            cls("g_c_e_a_or_l_or_equal"),
        ]
