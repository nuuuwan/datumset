from ds.thing.concept.CategoryConcept import CategoryConcept


class Religion(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'buddhist',
            'hindu',
            'islam',
            'other',
            'other_christian',
            'roman_catholic',
        ]

    @classmethod
    def get_color_map(cls):
        return {
            'buddhist': '#FFBE29',
            'hindu': '#DF7500',
            'islam': '#005F56',
            'other': '#cccccc',
            'other_christian': '#2980b9',
            'roman_catholic': '#8e44ad',
        }
