from ds.thing.concept.CategoryConcept import CategoryConcept


class EmmigrationReason(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'education',
            'employment',
            'family_in_need',
            'other',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'family_in_need': [
                'accompanying_family_member_in_need',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'education': '#3840D0',
            'employment': '#D05D38',
            'family_in_need': '#6CD038',
            'other': '#cccccc',
        }
