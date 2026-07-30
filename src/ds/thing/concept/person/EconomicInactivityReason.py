from ds.thing.concept.CategoryConcept import CategoryConcept


class EconomicInactivityReason(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'education_training',
            'household_work',
            'illness_or_disabled',
            'income_recipient',
            'not_interested',
            'other',
            'unable_or_retired',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'education_training': [
                'engage_in_educational_or_vocational_training',
            ],
            'household_work': [
                'engaged_in_household_work_or_childcare_or_elder_care',
            ],
            'illness_or_disabled': [
                'long_term_illness_or_disabled',
            ],
            'income_recipient': [
                'income_recipient_such_as_from_investment_rental_and_interest',
            ],
            'not_interested': [
                'does_not_want_or_interest_to_do_any_economic_activity',
            ],
            'unable_or_retired': [
                'unable_or_too_old_to_work_or_retired',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'education_training': '#3840D0',
            'household_work': '#D05D38',
            'illness_or_disabled': '#D03899',
            'income_recipient': '#D0AF38',
            'not_interested': '#38C5D0',
            'other': '#cccccc',
            'unable_or_retired': '#6CD038',
        }
