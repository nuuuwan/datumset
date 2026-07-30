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

    @classmethod
    def get_color_map(cls):
        return {
            "marriage": "#D05D38",
            "employment_searching_for_job": "#3840D0",
            "education": "#6CD038",
            "accompanied_a_family_member": "#D03899",
            "returning_for_permanent_residence": "#38C5D0",
            "development_projects": "#D0AF38",
            "resettled_after_displacement": "#8238D0",
            "a_disaster_a_displaced_happened_in_the_prior_place": "#38D056",
            "other": "#cccccc",
        }
