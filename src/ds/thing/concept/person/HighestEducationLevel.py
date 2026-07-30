from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "primary",
            "secondary",
            "gce_ordinary_level",
            "gce_advanced_level",
            "degree_and_above",
            "no_schooling",
            #
            "passed_grade_1_5",
            "passed_grade_6_8",
            "passed_grade_9_10",
            #
            "g_c_e_o_or_l_or_equivalent",
            "g_c_e_a_or_l_or_equivalent",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "never_attended_school": "no_schooling",
            "g_c_e_o_or_l_or_equal": "g_c_e_o_or_l_or_equivalent",
            "g_c_e_a_or_l_or_equal": "g_c_e_a_or_l_or_equivalent",
        }
