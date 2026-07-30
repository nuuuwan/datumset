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
            "contributing_to_family_enterprise": "contributing_to_family"
            + "_enterprise_unpaid_family_worker",
            "own_account_worker": "own_account_worker_don't_have_employees",
            "private_sector_paid_employee": "paid_employee_private_sector",
            "employer": "employer_have_employees",
        }
