from ds.thing.concept.CategoryConcept import CategoryConcept


class IsEconomicallyActive(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "employed",
            "unemployed",
            "economically_not_active",
            "economically_active",
            "economically_inactive",
        ]
