from ds.thing.concept.CategoryConcept import CategoryConcept

class Sex(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['both_sexes', 'female', 'male']

    @classmethod
    def get_color_map(cls):
        return {'both_sexes': '#6CD038', 'female': '#3840D0', 'male': '#D05D38'}