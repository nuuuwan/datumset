# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationReason(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "marriage",
            "employment_searching_for_job",
            "education",
            "accompanied_a_family_member",
            "returning_for_permanent_residence",
            # 6 - 9
            "development_projects",
            "resettled_after_displacement",
            "a_disaster_a_displaced_happened_in_the_prior_place",
            "other",
        ]
