from ds.thing.concept.CategoryConcept import CategoryConcept

class Sector(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['estate', 'estate_rural', 'estate_urban', 'rural', 'urban']

    @classmethod
    def get_color_map(cls):
        return {'estate': '#6CD038', 'estate_rural': '#D03899', 'estate_urban': '#38C5D0', 'rural': '#3840D0', 'urban': '#D05D38'}