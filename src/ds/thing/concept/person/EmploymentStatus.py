# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmploymentStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "government_paid_employee",
            "semi_government_paid_employee",
            "paid_employee_private_sector",
            "employer_have_employees",
            "own_account_worker_don't_have_employees",
            "contributing_to_family_enterprise_unpaid_family_worker",
            #
            "government_or_semi_government_paid_employee",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "contributing_to_family_enterprise_unpaid_family_worker": [
                "contributing_to_family_enterprise"
            ],
            "own_account_worker_don't_have_employees": ["own_account_worker"],
            "paid_employee_private_sector": ["private_sector_paid_employee"],
            "employer_have_employees": ["employer"],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "government_paid_employee": "#D05D38",
            "semi_government_paid_employee": "#3840D0",
            "paid_employee_private_sector": "#6CD038",
            "employer_have_employees": "#D03899",
            "own_account_worker_don't_have_employees": "#38C5D0",
            "contributing_to_family_enterprise_unpaid_family_worker": "#D0AF38",
            "government_or_semi_government_paid_employee": "#8238D0",
        }
