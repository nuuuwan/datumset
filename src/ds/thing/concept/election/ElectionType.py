from ds.thing.concept.CategoryConcept import CategoryConcept

class ElectionType(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['local_government', 'parliamentary', 'presidential']

    @classmethod
    def get_color_map(cls):
        return {'local_government': '#6CD038', 'parliamentary': '#D05D38', 'presidential': '#3840D0'}