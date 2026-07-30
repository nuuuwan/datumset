from ds.thing.concept.CategoryConcept import CategoryConcept


class WallType(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'bricks',
            'cabook',
            'cadjan_palmyrah',
            'cement_block',
            'cement_block_stone',
            'granite_cube_stones',
            'not_relevant',
            'other',
            'plank_or_metal_sheet',
            'planks_metal',
            'pressed_soil_bricks',
            'warichchi_mud',
            'zink_aluminium',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'bricks': [
                'brick',
            ],
            'cadjan_palmyrah': [
                'cadjan_or_palmyrah',
            ],
            'cement_block_stone': [
                'cement_block_or_stone',
            ],
            'planks_metal': [
                'planks_metal_sheets_asbestos',
            ],
            'pressed_soil_bricks': [
                'soil_bricks',
            ],
            'warichchi_mud': [
                'mud',
            ],
            'zink_aluminium': [
                'zink_aluminium_sheets',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'bricks': '#D05D38',
            'cabook': '#6CD038',
            'cadjan_palmyrah': '#D0AF38',
            'cement_block': '#38D056',
            'cement_block_stone': '#3840D0',
            'granite_cube_stones': '#D03847',
            'not_relevant': '#cccccc',
            'other': '#cccccc',
            'plank_or_metal_sheet': '#8238D0',
            'planks_metal': '#3873D0',
            'pressed_soil_bricks': '#D03899',
            'warichchi_mud': '#38C5D0',
            'zink_aluminium': '#9FD038',
        }
