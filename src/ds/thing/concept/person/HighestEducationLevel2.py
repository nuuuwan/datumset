from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel2(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "never_attended",
            "special_school",
            "passed_grade_1_5",
            "passed_grade_6_8",
            "passed_grade_9_10",
            "passed_gce_o_or_l",
            "passed_gce_a_or_l",
            "degree_or_above",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "never_attended": [
                "never_attended_school",
            ],
            "special_school": [
                "studied_in_a_special_school_or_special_unit",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "never_attended": "#D05D38",
            "special_school": "#3840D0",
            "passed_grade_1_5": "#6CD038",
            "passed_grade_6_8": "#D03899",
            "passed_grade_9_10": "#38C5D0",
            "passed_gce_o_or_l": "#D0AF38",
            "passed_gce_a_or_l": "#8238D0",
            "degree_or_above": "#38D056",
        }
