from ds.thing.concept.CategoryConcept import CategoryConcept


class MaritalStatus(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'divorced',
            'legally_separated',
            'married',
            'married_customary',
            'married_registered',
            'never_married',
            'not_stated',
            'separated_not_legal',
            'widowed',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'separated_not_legal': [
                'separated_not_legally',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'divorced': '#D0AF38',
            'legally_separated': '#8238D0',
            'married': '#D03899',
            'married_customary': '#6CD038',
            'married_registered': '#3840D0',
            'never_married': '#D05D38',
            'not_stated': '#cccccc',
            'separated_not_legal': '#38D056',
            'widowed': '#38C5D0',
        }
