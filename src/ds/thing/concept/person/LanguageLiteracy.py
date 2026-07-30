from ds.thing.concept.CategoryConcept import CategoryConcept


class LanguageLiteracy(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'any_language',
            'english',
            'sinhala',
            'tamil',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'any_language': [
                'at_least_one_language',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'any_language': '#D05D38',
            'english': '#D03899',
            'sinhala': '#3840D0',
            'tamil': '#6CD038',
        }
