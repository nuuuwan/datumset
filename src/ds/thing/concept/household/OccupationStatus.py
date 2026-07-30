from ds.thing.concept.CategoryConcept import CategoryConcept


class OccupationStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "occupied",
            "vacant",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "occupied": "#D05D38",
            "vacant": "#3840D0",
        }
