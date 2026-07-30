from ds.thing.concept.CategoryConcept import CategoryConcept


class TypeOfUnit(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'improvised',
            'not_permanent',
            'permanent',
            'semi_permanent',
            'unclassified',
        ]

    @classmethod
    def get_color_map(cls):
        return {
            'improvised': '#D03899',
            'not_permanent': '#3840D0',
            'permanent': '#D05D38',
            'semi_permanent': '#6CD038',
            'unclassified': '#cccccc',
        }
