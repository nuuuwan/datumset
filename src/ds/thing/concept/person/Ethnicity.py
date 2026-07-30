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
            "veddha": "veddahs",
            "sinhalese": "sinhala",
            "sl_tamil": "sri_lanka_tamil",
            "sri_lanka_muslim": "sri_lanka_moor_or_muslim",
            "sl_moor": "sri_lanka_moor_or_muslim",
            "sl_chetty": "sri_lanka_chetty",
            "ind_tamil": "ind_and_malaiyaga_tamil",
            "other_eth": "other",
            "indian_tamil": "ind_and_malaiyaga_tamil",
            "indian_malaiyaga_tamil": "ind_and_malaiyaga_tamil",
            "indian_tamil_or_malaiyaga_thamilar": "ind_and_malaiyaga_tamil",
            "sri_lanka_moor_muslim": "sri_lanka_moor_or_muslim",
        }

    @classmethod
    def get_color_map(cls):
        return {
            "sinhala": "#941E32",
            "sri_lanka_tamil": "#DF7500",
            "sri_lanka_moor_or_muslim": "#005F56",
            #
            "ind_and_malaiyaga_tamil": "#ff8888",
            "burgher": "#8e44ad",
            "malay": "#cccccc",
            #
            "sri_lanka_chetty": "#e67e22",
            "bharatha": "#16a085",
            "veddahs": "#795548",
            "other": "#999999",
            # legacy
            "indian_muslim": "#00897b",
            "european": "#6c5ce7",
            "burgher_and_eurasian": "#9b59b6",
            "low_country_sinhalese": "#c0392b",
            "up_country_kandyan_sinhalese": "#e74c3c",
        }
