# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class DisabilityTypes(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("DifficultyInSeeing"),
            cls("DifficultyInHearing"),
            cls("DifficultyInWalkingOrClimbingSteps"),
            cls("DifficultyInRememberingOrConcentrating"),
            cls("DifficultyInSelfcareSuchAsWashingOrDressing"),
            # 6 - 7
            cls("DifficultyInCommunicatingWithOthers"),
            cls("NoDisability"),
        ]
