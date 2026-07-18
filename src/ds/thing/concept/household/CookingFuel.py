from ds.thing.concept.CategoryConcept import CategoryConcept


class CookingFuel(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("FireWood"),
            cls("Kerosene"),
            cls("Gas"),
            cls("Electricity"),
            cls("SawDustOrPaddyHusk"),
            cls("Other"),
        ]
