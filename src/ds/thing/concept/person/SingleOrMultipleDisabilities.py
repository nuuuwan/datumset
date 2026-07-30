from ds.thing.concept.CategoryConcept import CategoryConcept


class SingleOrMultipleDisabilities(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "single_disability",
            "multi_disability",
            "no_disability",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "multi_disability": [
                "with_more_than_one_disability",
                "multiple_disabilities",
            ],
            "single_disability": [
                "with_single_disability",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "single_disability": "#D05D38",
            "multi_disability": "#3840D0",
            "no_disability": "#cccccc",
        }
