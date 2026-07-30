from ds.thing.concept.CategoryConcept import CategoryConcept


class Sex(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "male",
            "female",
            "both_sexes",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "male": "#D05D38",
            "female": "#3840D0",
            "both_sexes": "#6CD038",
        }
