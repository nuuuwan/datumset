from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel3(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "no_schooling",
            "passed_1_5_years",
            "passed_6_10_years",
            "gce_ol",
            "gce_al",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "no_schooling": "#D05D38",
            "passed_1_5_years": "#3840D0",
            "passed_6_10_years": "#6CD038",
            "gce_ol": "#D03899",
            "gce_al": "#38C5D0",
        }
