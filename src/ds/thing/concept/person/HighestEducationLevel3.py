from ds.thing.concept.CategoryConcept import CategoryConcept

class HighestEducationLevel3(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['gce_al', 'gce_ol', 'no_schooling', 'passed_1_5_years', 'passed_6_10_years']

    @classmethod
    def get_color_map(cls):
        return {'gce_al': '#38C5D0', 'gce_ol': '#D03899', 'no_schooling': '#D05D38', 'passed_1_5_years': '#3840D0', 'passed_6_10_years': '#6CD038'}