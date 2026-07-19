# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusTopic(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("schedule"),
            cls("demographic_and_personal_information"),
            cls("name"),
            cls("relationship_to_head_of_the_household"),
            cls("sex"),
            # 6 - 10
            cls("date_of_birth"),
            cls("age"),
            cls("marital_status"),
            cls("ethnic_group"),
            cls("religion"),
            # 11 - 15
            cls("citizenship"),
            cls("n_i_c_no_"),
            cls("status_of_clergy_or_priest"),
            cls("educational_characteristics"),
            cls("ability_to_speak_sinhala_and_tamil"),
            # 16 - 20
            cls("ability_to_speak_english"),
            cls("ability_to_speak_sinhala_english_and_tamil"),
            cls("literacy"),
            cls("english_literacy"),
            cls("sinhala_english_and_tamil_literacy"),
            # 21 - 25
            cls("computer_literacy"),
            cls("digital_literacy"),
            cls("educational_attainment_or_highest_level_of"),
            cls("school_attendance_or_attend_in_educational"),
            cls("vocational_and_apprenticeship_qualification"),
        ]
