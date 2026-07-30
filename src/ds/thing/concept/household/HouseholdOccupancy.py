from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdOccupancy(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'closed_or_vacant',
            'occupied',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'closed_or_vacant': [
                'permanently_closed_or_vacant',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'closed_or_vacant': '#3840D0',
            'occupied': '#D05D38',
        }
