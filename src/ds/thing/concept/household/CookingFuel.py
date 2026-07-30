from ds.thing.concept.CategoryConcept import CategoryConcept

class CookingFuel(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['bio_gas', 'electricity', 'fire_wood', 'gas', 'kerosene', 'not_relevant', 'other', 'sawdust_paddy_husk']

    @classmethod
    def map_alias(cls):
        return {'fire_wood': ['firewood'], 'sawdust_paddy_husk': ['saw_dust_or_paddy_husk']}

    @classmethod
    def get_color_map(cls):
        return {'bio_gas': '#D0AF38', 'electricity': '#D03899', 'fire_wood': '#D05D38', 'gas': '#6CD038', 'kerosene': '#3840D0', 'not_relevant': '#cccccc', 'other': '#cccccc', 'sawdust_paddy_husk': '#38C5D0'}