from ds.thing.concept.CategoryConcept import CategoryConcept

class LivingQuarters(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['collective_quarter', 'housing_unit', 'non_housing_unit']

    @classmethod
    def map_alias(cls):
        return {'collective_quarter': ['collective_living_quarter']}

    @classmethod
    def get_color_map(cls):
        return {'collective_quarter': '#3840D0', 'housing_unit': '#D05D38', 'non_housing_unit': '#6CD038'}