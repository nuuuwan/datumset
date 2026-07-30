from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationReason(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "marriage",
            "job_search",
            "education",
            "family_accompanied",
            "permanent_return",
            "development_projects",
            "resettled",
            "disaster_displaced",
            "other",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "disaster_displaced": [
                "a_disaster_a_displaced_happened_in_the_prior_place",
            ],
            "family_accompanied": [
                "accompanied_a_family_member",
            ],
            "job_search": [
                "employment_searching_for_job",
            ],
            "permanent_return": [
                "returning_for_permanent_residence",
            ],
            "resettled": [
                "resettled_after_displacement",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "marriage": "#D05D38",
            "job_search": "#3840D0",
            "education": "#6CD038",
            "family_accompanied": "#D03899",
            "permanent_return": "#38C5D0",
            "development_projects": "#D0AF38",
            "resettled": "#8238D0",
            "disaster_displaced": "#38D056",
            "other": "#cccccc",
        }
