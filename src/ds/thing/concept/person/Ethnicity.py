from ds.thing.concept.CategoryConcept import CategoryConcept


class Ethnicity(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            "sinhala",
            "sri_lanka_tamil",
            "ind_and_malaiyaga_tamil",
            "sri_lanka_moor_or_muslim",
            "burgher",
            "malay",
            "sri_lanka_chetty",
            "bharatha",
            "other_eth",
            "veddahs",
            "other",
            # legacy
            "indian_muslim",
            "european",
            "burgher_and_eurasian",
            "low_country_sinhalese",
            "up_country_kandyan_sinhalese",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "veddas": "veddahs",
            "sinhalese": "sinhala",
            "sl_tamil": "sri_lanka_tamil",
            "sl_moor": "sri_lanka_moor_or_muslim",
            "sl_chetty": "sri_lanka_chetty",
        }
