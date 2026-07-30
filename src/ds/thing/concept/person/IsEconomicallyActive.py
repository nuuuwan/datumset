from ds.thing.concept.CategoryConcept import CategoryConcept


class IsEconomicallyActive(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "employed",
            "unemployed",
            "economically_active",
            "economically_inactive",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "economically_not_active": "economically_inactive",
        }
