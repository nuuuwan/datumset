from ds.thing.concept.CategoryConcept import CategoryConcept


class DisabilityTypes(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "difficulty_in_seeing",
            "difficulty_in_hearing",
            "difficulty_in_walking_or_climbing_steps",
            "difficulty_in_remembering_or_concentrating",
            "difficulty_in_selfcare_such_as_washing_or_dressing",
            # 6 - 7
            "difficulty_in_communicating_with_others",
            "no_disability",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "difficulty_in_seeing": "#D05D38",
            "difficulty_in_hearing": "#3840D0",
            "difficulty_in_walking_or_climbing_steps": "#6CD038",
            "difficulty_in_remembering_or_concentrating": "#D03899",
            "difficulty_in_selfcare_such_as_washing_or_dressing": "#38C5D0",
            "difficulty_in_communicating_with_others": "#D0AF38",
            "no_disability": "#cccccc",
        }
