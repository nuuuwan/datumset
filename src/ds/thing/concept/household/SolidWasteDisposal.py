from ds.thing.concept.CategoryConcept import CategoryConcept

class SolidWasteDisposal(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return ['dispose_outdoors', 'local_collected', 'occupants_burn', 'occupants_bury', 'occupants_compost', 'other']

    @classmethod
    def map_alias(cls):
        return {'dispose_outdoors': ['occupants_dispose_solid_waste_into_road_or_river_or_canal_or_sea_or_creek_or_forest_etc'], 'local_collected': ['collected_by_local_authorities'], 'occupants_compost': ['occupants_composting_solid_waste']}

    @classmethod
    def get_color_map(cls):
        return {'dispose_outdoors': '#38C5D0', 'local_collected': '#D05D38', 'occupants_burn': '#3840D0', 'occupants_bury': '#6CD038', 'occupants_compost': '#D03899', 'other': '#cccccc'}