from ds.thing.concept.CategoryConcept import CategoryConcept


class CookingFuel(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "fire_wood",
            "kerosene",
            "gas",
            "electricity",
            "saw_dust_or_paddy_husk",
            "other",
        ]
