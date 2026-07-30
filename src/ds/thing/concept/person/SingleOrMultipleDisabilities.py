from ds.thing.concept.CategoryConcept import CategoryConcept

class SingleOrMultipleDisabilities(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['multi_disability', 'no_disability', 'single_disability']

    @classmethod
    def map_alias(cls):
        return {'multi_disability': ['multiple_disabilities', 'with_more_than_one_disability'], 'single_disability': ['with_single_disability']}

    @classmethod
    def get_color_map(cls):
        return {'multi_disability': '#3840D0', 'no_disability': '#cccccc', 'single_disability': '#D05D38'}