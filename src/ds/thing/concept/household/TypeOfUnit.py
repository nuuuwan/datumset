from ds.thing.concept.CategoryConcept import CategoryConcept


class TypeOfUnit(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "permanent",
            "not_permanent",
            "semi_permanent",
            "improvised",
            "unclassified",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "permanent": "#D05D38",
            "not_permanent": "#3840D0",
            "semi_permanent": "#6CD038",
            "improvised": "#D03899",
            "unclassified": "#cccccc",
        }
