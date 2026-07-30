from ds.thing.concept.CategoryConcept import CategoryConcept


class EmploymentStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "govt_employee",
            "semi_govt_employee",
            "private_employee",
            "employer",
            "own_account_worker",
            "family_enterprise",
            "govt_or_semi_govt",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "employer": [
                "employer_have_employees",
            ],
            "family_enterprise": [
                "contributing_to_family_enterprise",
                "contributing_to_family_enterprise_unpaid_family_worker",
            ],
            "govt_employee": [
                "government_paid_employee",
            ],
            "govt_or_semi_govt": [
                "government_or_semi_government_paid_employee",
            ],
            "own_account_worker": [
                "own_account_worker_don't_have_employees",
            ],
            "private_employee": [
                "private_sector_paid_employee",
                "paid_employee_private_sector",
            ],
            "semi_govt_employee": [
                "semi_government_paid_employee",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "govt_employee": "#D05D38",
            "semi_govt_employee": "#3840D0",
            "private_employee": "#6CD038",
            "employer": "#D03899",
            "own_account_worker": "#38C5D0",
            "family_enterprise": "#D0AF38",
            "govt_or_semi_govt": "#8238D0",
        }
