from ds.thing.concept.CategoryConcept import CategoryConcept


class IsEconomicallyActive(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "employed",
            "unemployed",
            "economically_active",
            "inactive",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "inactive": [
                "economically_not_active",
                "economically_inactive",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "employed": "#D05D38",
            "unemployed": "#3840D0",
            "economically_active": "#6CD038",
            "inactive": "#D03899",
        }
