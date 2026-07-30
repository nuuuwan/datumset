from ds.thing.concept.CategoryConcept import CategoryConcept


class OneRoomOrMore(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'more_than_one_room',
            'with_only_one_room',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'more_than_one_room': [
                'with_only_more_than_one_room',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'more_than_one_room': '#3840D0',
            'with_only_one_room': '#D05D38',
        }
