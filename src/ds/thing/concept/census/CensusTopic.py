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
            "n_i_c_no_",
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
