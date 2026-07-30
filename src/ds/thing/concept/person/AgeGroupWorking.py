from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupWorking(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'age_20_64',
            'age_65_above',
            'age_below_20',
        ]

    @classmethod
    def get_color_map(cls):
        return {
            'age_20_64': '#3840D0',
            'age_65_above': '#6CD038',
            'age_below_20': '#D05D38',
        }
