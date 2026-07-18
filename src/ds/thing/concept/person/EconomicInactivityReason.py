# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EconomicInactivityReason(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("EngagedInHouseholdWorkOrChildcareOrElderCare"),
            cls("EngageInEducationalOrVocationalTraining"),
            cls("UnableOrTooOldToWorkOrRetired"),
            cls("LongTermIllnessOrDisabled"),
            cls("DoesNotWantOrInterestToDoAnyEconomicActivity"),
            # 6 - 7
            cls("Other"),
            cls("IncomeRecipientSuchAsFromInvestmentRentalAndInterest"),
        ]
