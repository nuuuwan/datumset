from ds.thing.concept.CategoryConcept import CategoryConcept


class Ethnicity(CategoryConcept):

    @classmethod
    def list(cls):
        return (
            cls("sinhalese"),
            cls("sl_tamil"),
            cls("ind_tamil"),
            cls("sl_moor"),
            cls("burgher"),
            cls("malay"),
            cls("sl_chetty"),
            cls("bharatha"),
            cls("other_eth"),
            # legacy
            cls("indian_muslim"),
            cls("european"),
            cls("burgher_and_eurasian"),
            cls("low_country_sinhalese"),
            cls("up_country_kandyan_sinhalese"),
        )

    @classmethod
    def map_alias(cls, value):
        from ds.thing.concept.CategoryConcept import CategoryConcept

        return {
            "Sri Lanka Chetty": "sl_chetty",
            "Other": "other_eth",
            "Sri Lanka Moor/Muslim": "sl_moor",
            "Sri Lanka Muslim": "sl_moor",
            "Indian Tamil/Malaiyaga Thamilar": "ind_tamil",
            "Sri Lanka Tamil": "sl_tamil",
            "Indian Tamil": "ind_tamil",
        }.get(value, CategoryConcept.map_alias(value))
