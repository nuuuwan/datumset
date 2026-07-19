# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationReason(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("marriage"),
            cls("employment_searching_for_job"),
            cls("education"),
            cls("accompanied_a_family_member"),
            cls("returning_for_permanent_residence"),
            # 6 - 9
            cls("development_projects"),
            cls("resettled_after_displacement"),
            cls("a_disaster_a_displaced_happened_in_the_prior_place"),
            cls("other"),
        ]
