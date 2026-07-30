from ds.thing.concept.CategoryConcept import CategoryConcept


class LanguageLiteracy(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 4
            "at_least_one_language",
            "sinhala",
            "tamil",
            "english",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "at_least_one_language": "#D05D38",
            "sinhala": "#3840D0",
            "tamil": "#6CD038",
            "english": "#D03899",
        }
