from ds.thing.concept.CategoryConcept import CategoryConcept


class FloorType(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'cement',
            'concrete',
            'mud',
            'not_relevant',
            'other',
            'sand',
            'terrazzo_wood',
            'tile_granite_terra',
            'wood',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'terrazzo_wood': [
                'terrazzo_tile_granite_wood_finished',
            ],
            'tile_granite_terra': [
                'tile_or_granite_or_terrazo',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'cement': '#D05D38',
            'concrete': '#D0AF38',
            'mud': '#6CD038',
            'not_relevant': '#cccccc',
            'other': '#cccccc',
            'sand': '#38C5D0',
            'terrazzo_wood': '#8238D0',
            'tile_granite_terra': '#3840D0',
            'wood': '#D03899',
        }
