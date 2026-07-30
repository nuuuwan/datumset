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

    @classmethod
    def get_color_map(cls):
        return {
            "engaged_in_household_work_or_childcare_or_elder_care": "#D05D38",
            "engage_in_educational_or_vocational_training": "#3840D0",
            "unable_or_too_old_to_work_or_retired": "#6CD038",
            "long_term_illness_or_disabled": "#D03899",
            "does_not_want_or_interest_to_do_any_economic_activity": "#38C5D0",
            "other": "#cccccc",
            "income_recipient_such_as_from_investment_rental_and_interest": "#D0AF38",  # noqa: E501
        }
