from ds.thing.concept.CategoryConcept import CategoryConcept


class AdministrativeEntity(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "assistant_government_agend_divisions",
            "grama_sevaka_divisions",
            "municipal_councils",
            "urban_councils",
            "town_councils",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "assistant_government_agend_divisions": "#D05D38",
            "grama_sevaka_divisions": "#3840D0",
            "municipal_councils": "#6CD038",
            "urban_councils": "#D03899",
            "town_councils": "#38C5D0",
        }
