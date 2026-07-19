from ds.thing.concept.CategoryConcept import CategoryConcept


class IsEconomicallyActive(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Employed"),
            cls("Unemployed"),
            cls("EconomicallyNotActive"),
            cls("EconomicallyActive"),
            cls("EconomicallyInactive"),
        ]
