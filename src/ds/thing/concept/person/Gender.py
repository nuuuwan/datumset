from ds.thing.concept.CategoryConcept import CategoryConcept


class Gender(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "male",
            "female",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "male": "#D05D38",
            "female": "#3840D0",
        }
