# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmploymentStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("government_paid_employee"),
            cls("semi_government_paid_employee"),
            cls("paid_employee_private_sector"),
            cls("employer_have_employees"),
            cls("own_account_worker_don't_have_employees"),
            cls("contributing_to_family_enterprise_unpaid_family_worker"),
        ]
