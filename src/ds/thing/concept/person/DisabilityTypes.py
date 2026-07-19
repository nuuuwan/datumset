# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class DisabilityTypes(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("difficulty_in_seeing"),
            cls("difficulty_in_hearing"),
            cls("difficulty_in_walking_or_climbing_steps"),
            cls("difficulty_in_remembering_or_concentrating"),
            cls("difficulty_in_selfcare_such_as_washing_or_dressing"),
            # 6 - 7
            cls("difficulty_in_communicating_with_others"),
            cls("no_disability"),
        ]
