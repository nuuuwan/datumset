from ds.thing.concept.CategoryConcept import CategoryConcept


class EmploymentStatus(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'employer',
            'family_enterprise',
            'govt_employee',
            'govt_or_semi_govt',
            'own_account_worker',
            'private_employee',
            'semi_govt_employee',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'employer': [
                'employer_have_employees',
            ],
            'family_enterprise': [
                'contributing_to_family_enterprise',
                'contributing_to_family_enterprise_unpaid_family_worker',
            ],
            'govt_employee': [
                'government_paid_employee',
            ],
            'govt_or_semi_govt': [
                'government_or_semi_government_paid_employee',
            ],
            'own_account_worker': [
                "own_account_worker_don't_have_employees",
            ],
            'private_employee': [
                'paid_employee_private_sector',
                'private_sector_paid_employee',
            ],
            'semi_govt_employee': [
                'semi_government_paid_employee',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'employer': '#D03899',
            'family_enterprise': '#D0AF38',
            'govt_employee': '#D05D38',
            'govt_or_semi_govt': '#8238D0',
            'own_account_worker': '#38C5D0',
            'private_employee': '#6CD038',
            'semi_govt_employee': '#3840D0',
        }
