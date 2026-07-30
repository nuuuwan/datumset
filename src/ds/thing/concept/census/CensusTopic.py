from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusTopic(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "schedule",
            "demographic_info",
            "name",
            "relationship_head",
            "sex",
            "date_of_birth",
            "age",
            "marital_status",
            "ethnic_group",
            "religion",
            "citizenship",
            "n_i_c_no",
            "clergy_or_priest",
            "education_chars",
            "speak_sinhala_tamil",
            "speak_english",
            "speak_all_languages",
            "literacy",
            "english_literacy",
            "all_literacy",
            "computer_literacy",
            "digital_literacy",
            "education_attainment",
            "school_attendance",
            "vocational_quals",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "all_literacy": [
                "sinhala_english_and_tamil_literacy",
            ],
            "clergy_or_priest": [
                "status_of_clergy_or_priest",
            ],
            "demographic_info": [
                "demographic_and_personal_information",
            ],
            "education_attainment": [
                "educational_attainment_or_highest_level_of",
            ],
            "education_chars": [
                "educational_characteristics",
            ],
            "relationship_head": [
                "relationship_to_head_of_the_household",
            ],
            "school_attendance": [
                "school_attendance_or_attend_in_educational",
            ],
            "speak_all_languages": [
                "ability_to_speak_sinhala_english_and_tamil",
            ],
            "speak_english": [
                "ability_to_speak_english",
            ],
            "speak_sinhala_tamil": [
                "ability_to_speak_sinhala_and_tamil",
            ],
            "vocational_quals": [
                "vocational_and_apprenticeship_qualification",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "schedule": "#D05D38",
            "demographic_info": "#3840D0",
            "name": "#6CD038",
            "relationship_head": "#D03899",
            "sex": "#38C5D0",
            "date_of_birth": "#D0AF38",
            "age": "#8238D0",
            "marital_status": "#38D056",
            "ethnic_group": "#D03847",
            "religion": "#3873D0",
            "citizenship": "#9FD038",
            "n_i_c_no": "#D038CB",
            "clergy_or_priest": "#38D0A8",
            "education_chars": "#D07C38",
            "speak_sinhala_tamil": "#5038D0",
            "speak_english": "#4DD038",
            "speak_all_languages": "#D03879",
            "literacy": "#38A6D0",
            "english_literacy": "#D0CE38",
            "all_literacy": "#A238D0",
            "computer_literacy": "#38D076",
            "digital_literacy": "#D04938",
            "education_attainment": "#3853D0",
            "school_attendance": "#80D038",
            "vocational_quals": "#D038AC",
        }
