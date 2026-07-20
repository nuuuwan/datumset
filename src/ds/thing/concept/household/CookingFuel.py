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
            #
            "bio_gas",
            "not_relevant",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "firewood": "fire_wood",
            "sawdust_paddy_husk": "saw_dust_or_paddy_husk",
        }
