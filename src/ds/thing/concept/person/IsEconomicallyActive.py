from ds.thing.concept.CategoryConcept import CategoryConcept

class IsEconomicallyActive(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['economically_active', 'employed', 'inactive', 'unemployed']

    @classmethod
    def map_alias(cls):
        return {'inactive': ['economically_inactive', 'economically_not_active']}

    @classmethod
    def get_color_map(cls):
        return {'economically_active': '#6CD038', 'employed': '#D05D38', 'inactive': '#D03899', 'unemployed': '#3840D0'}