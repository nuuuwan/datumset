from ds.thing.concept.CategoryConcept import CategoryConcept


class WallType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "bricks",
            "cement_block_stone",
            "cabook",
            "pressed_soil_bricks",
            "warichchi_mud",
            "cadjan_palmyrah",
            "plank_or_metal_sheet",
            "other",
            "cement_block",
            "granite_cube_stones",
            "planks_metal",
            "zink_aluminium",
            "not_relevant",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "bricks": [
                "brick",
            ],
            "cadjan_palmyrah": [
                "cadjan_or_palmyrah",
            ],
            "cement_block_stone": [
                "cement_block_or_stone",
            ],
            "planks_metal": [
                "planks_metal_sheets_asbestos",
            ],
            "pressed_soil_bricks": [
                "soil_bricks",
            ],
            "warichchi_mud": [
                "mud",
            ],
            "zink_aluminium": [
                "zink_aluminium_sheets",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "bricks": "#D05D38",
            "cement_block_stone": "#3840D0",
            "cabook": "#6CD038",
            "pressed_soil_bricks": "#D03899",
            "warichchi_mud": "#38C5D0",
            "cadjan_palmyrah": "#D0AF38",
            "plank_or_metal_sheet": "#8238D0",
            "other": "#cccccc",
            "cement_block": "#38D056",
            "granite_cube_stones": "#D03847",
            "planks_metal": "#3873D0",
            "zink_aluminium": "#9FD038",
            "not_relevant": "#cccccc",
        }
