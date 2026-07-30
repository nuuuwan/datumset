# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusTopic(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "schedule",
            "demographic_and_personal_information",
            "name",
            "relationship_to_head_of_the_household",
            "sex",
            # 6 - 10
            "date_of_birth",
            "age",
            "marital_status",
            "ethnic_group",
            "religion",
            # 11 - 15
            "citizenship",
            "n_i_c_no",
            "status_of_clergy_or_priest",
            "educational_characteristics",
            "ability_to_speak_sinhala_and_tamil",
            # 16 - 20
            "ability_to_speak_english",
            "ability_to_speak_sinhala_english_and_tamil",
            "literacy",
            "english_literacy",
            "sinhala_english_and_tamil_literacy",
            # 21 - 25
            "computer_literacy",
            "digital_literacy",
            "educational_attainment_or_highest_level_of",
            "school_attendance_or_attend_in_educational",
            "vocational_and_apprenticeship_qualification",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "schedule": "#D05D38",
            "demographic_and_personal_information": "#3840D0",
            "name": "#6CD038",
            "relationship_to_head_of_the_household": "#D03899",
            "sex": "#38C5D0",
            "date_of_birth": "#D0AF38",
            "age": "#8238D0",
            "marital_status": "#38D056",
            "ethnic_group": "#D03847",
            "religion": "#3873D0",
            "citizenship": "#9FD038",
            "n_i_c_no": "#D038CB",
            "status_of_clergy_or_priest": "#38D0A8",
            "educational_characteristics": "#D07C38",
            "ability_to_speak_sinhala_and_tamil": "#5038D0",
            "ability_to_speak_english": "#4DD038",
            "ability_to_speak_sinhala_english_and_tamil": "#D03879",
            "literacy": "#38A6D0",
            "english_literacy": "#D0CE38",
            "sinhala_english_and_tamil_literacy": "#A238D0",
            "computer_literacy": "#38D076",
            "digital_literacy": "#D04938",
            "educational_attainment_or_highest_level_of": "#3853D0",
            "school_attendance_or_attend_in_educational": "#80D038",
            "vocational_and_apprenticeship_qualification": "#D038AC",
        }
