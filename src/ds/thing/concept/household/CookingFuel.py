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

    @classmethod
    def get_color_map(cls):
        return {
            "fire_wood": "#D05D38",
            "kerosene": "#3840D0",
            "gas": "#6CD038",
            "electricity": "#D03899",
            "saw_dust_or_paddy_husk": "#38C5D0",
            "other": "#cccccc",
            "bio_gas": "#D0AF38",
            "not_relevant": "#cccccc",
        }
