from ds.thing.concept.CategoryConcept import CategoryConcept


class WallType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "bricks",
            "cement_block_or_stone",
            "cabook",
            "pressed_soil_bricks",
            "warichchi_mud",
            "cadjan_palmyrah",
            "plank_or_metal_sheet",
            "other",
            #
            "cement_block",
            "granite_cube_stones",
            "planks_metal_sheets_asbestos",
            "zink_aluminium_sheets",
            "not_relevant",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "brick": "bricks",
            "soil_bricks": "pressed_soil_bricks",
            "mud": "warichchi_mud",
            "cadjan_or_palmyrah": "cadjan_palmyrah",
        }
