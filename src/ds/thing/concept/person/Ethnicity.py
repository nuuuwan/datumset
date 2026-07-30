from ds.thing.concept.CategoryConcept import CategoryConcept


class Ethnicity(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "sinhala",
            "sri_lanka_tamil",
            "indian_tamil",
            "sri_lanka_muslim",
            "burgher",
            "malay",
            "sri_lanka_chetty",
            "bharatha",
            "veddahs",
            "other",
            "indian_muslim",
            "european",
            "burgher_and_eurasian",
            "low_country_sinhala",
            "up_country_sinhala",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "indian_tamil": [
                "ind_tamil",
                "indian_malaiyaga_tamil",
                "indian_tamil_or_malaiyaga_thamilar",
                "ind_and_malaiyaga_tamil",
            ],
            "low_country_sinhala": [
                "low_country_sinhalese",
            ],
            "other": [
                "other_eth",
            ],
            "sinhala": [
                "sinhalese",
            ],
            "sri_lanka_chetty": [
                "sl_chetty",
            ],
            "sri_lanka_muslim": [
                "sl_moor",
                "sri_lanka_moor_muslim",
                "sri_lanka_moor_or_muslim",
            ],
            "sri_lanka_tamil": [
                "sl_tamil",
            ],
            "up_country_sinhala": [
                "up_country_kandyan_sinhalese",
            ],
            "veddahs": [
                "veddas",
                "veddha",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "sinhala": "#941E32",
            "sri_lanka_tamil": "#DF7500",
            "sri_lanka_muslim": "#005F56",
            "indian_tamil": "#ff8888",
            "burgher": "#8e44ad",
            "malay": "#cccccc",
            "sri_lanka_chetty": "#e67e22",
            "bharatha": "#16a085",
            "veddahs": "#795548",
            "other": "#999999",
            "indian_muslim": "#00897b",
            "european": "#6c5ce7",
            "burgher_and_eurasian": "#9b59b6",
            "low_country_sinhala": "#c0392b",
            "up_country_sinhala": "#e74c3c",
        }
