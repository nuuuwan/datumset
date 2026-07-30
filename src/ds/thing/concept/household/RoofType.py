from ds.thing.concept.CategoryConcept import CategoryConcept


class RoofType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "tile",
            "asbestos",
            "concrete",
            "zink_aluminium_sheet",
            "metal_sheet",
            "cadjan_palmyrah_straw",
            "other",
            #
            "not_relevant",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "cadjan_palmyrah_straw": ["cadjan_or_palmyrah_or_straw"],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "tile": "#D05D38",
            "asbestos": "#3840D0",
            "concrete": "#6CD038",
            "zink_aluminium_sheet": "#D03899",
            "metal_sheet": "#38C5D0",
            "cadjan_palmyrah_straw": "#D0AF38",
            "other": "#cccccc",
            "not_relevant": "#cccccc",
        }
