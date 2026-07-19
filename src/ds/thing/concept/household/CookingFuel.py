from ds.thing.concept.CategoryConcept import CategoryConcept


class CookingFuel(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("fire_wood"),
            cls("kerosene"),
            cls("gas"),
            cls("electricity"),
            cls("saw_dust_or_paddy_husk"),
            cls("other"),
        ]
