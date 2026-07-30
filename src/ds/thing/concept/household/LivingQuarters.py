from ds.thing.concept.CategoryConcept import CategoryConcept


class LivingQuarters(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "housing_unit",
            "collective_living_quarter",
            "non_housing_unit",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "housing_unit": "#D05D38",
            "collective_living_quarter": "#3840D0",
            "non_housing_unit": "#6CD038",
        }
