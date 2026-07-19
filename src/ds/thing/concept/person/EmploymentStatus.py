# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EmploymentStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("government_or_semi_government_paid_employee"),
            cls("private_sector_paid_employee"),
            cls("employer"),
            cls("own_account_worker"),
            cls("contributing_to_family_enterprise"),
        ]
