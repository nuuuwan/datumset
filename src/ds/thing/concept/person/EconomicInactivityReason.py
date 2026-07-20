# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EconomicInactivityReason(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "engaged_in_household_work_or_childcare_or_elder_care",
            "engage_in_educational_or_vocational_training",
            "unable_or_too_old_to_work_or_retired",
            "long_term_illness_or_disabled",
            "does_not_want_or_interest_to_do_any_economic_activity",
            # 6 - 7
            "other",
            "income_recipient_such_as_from_investment_rental_and_interest",
        ]
