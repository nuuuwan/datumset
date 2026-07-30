from ds.thing.concept.CategoryConcept import CategoryConcept

class HouseholdAppliances(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['bicycle', 'desktop_computer', 'fixed_line_telephone', 'internet_facilities', 'laptop_computer', 'motorcycle_scooter', 'normal_mobile_phone', 'other', 'radio', 'smart_mobile_phone', 'tablet_computer', 'television', 'three_wheeler']

    @classmethod
    def map_alias(cls):
        return {'motorcycle_scooter': ['motorcycle_or_scooter']}

    @classmethod
    def get_color_map(cls):
        return {'bicycle': '#3873D0', 'desktop_computer': '#D0AF38', 'fixed_line_telephone': '#6CD038', 'internet_facilities': '#D03847', 'laptop_computer': '#8238D0', 'motorcycle_scooter': '#9FD038', 'normal_mobile_phone': '#38C5D0', 'other': '#cccccc', 'radio': '#D05D38', 'smart_mobile_phone': '#D03899', 'tablet_computer': '#38D056', 'television': '#3840D0', 'three_wheeler': '#D038CB'}