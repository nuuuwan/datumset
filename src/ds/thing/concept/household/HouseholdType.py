from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdType(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'composite',
            'extended',
            'nuclear',
            'one_person',
        ]

    @classmethod
    def get_color_map(cls):
        return {
            'composite': '#D03899',
            'extended': '#6CD038',
            'nuclear': '#3840D0',
            'one_person': '#D05D38',
        }
