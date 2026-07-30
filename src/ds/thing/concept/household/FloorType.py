from ds.thing.concept.CategoryConcept import CategoryConcept


class FloorType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "cement",
            "tile_or_granite_or_terrazo",
            "mud",
            "wood",
            "sand",
            "concrete",
            "other",
            #
            "terrazzo_tile_granite_wood_finished",
            "not_relevant",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "cement": "#D05D38",
            "tile_or_granite_or_terrazo": "#3840D0",
            "mud": "#6CD038",
            "wood": "#D03899",
            "sand": "#38C5D0",
            "concrete": "#D0AF38",
            "other": "#cccccc",
            "terrazzo_tile_granite_wood_finished": "#8238D0",
            "not_relevant": "#cccccc",
        }
