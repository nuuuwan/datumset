from ds.thing.concept.CategoryConcept import CategoryConcept


class FloorType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "cement",
            "tile_granite_terra",
            "mud",
            "wood",
            "sand",
            "concrete",
            "other",
            "terrazzo_wood",
            "not_relevant",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "terrazzo_wood": [
                "terrazzo_tile_granite_wood_finished",
            ],
            "tile_granite_terra": [
                "tile_or_granite_or_terrazo",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "cement": "#D05D38",
            "tile_granite_terra": "#3840D0",
            "mud": "#6CD038",
            "wood": "#D03899",
            "sand": "#38C5D0",
            "concrete": "#D0AF38",
            "other": "#cccccc",
            "terrazzo_wood": "#8238D0",
            "not_relevant": "#cccccc",
        }
