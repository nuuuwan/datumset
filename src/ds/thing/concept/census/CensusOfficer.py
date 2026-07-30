from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusOfficer(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'area_supervisors',
            'asst_commissioners',
            'circle_officers',
            'deputy_commissioners',
            'divisional_officer',
            'enumerators_byoad',
            'enumerators_capi',
            'other_non_technical',
            'zonal_supervisors',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'area_supervisors': [
                'technical_staff_area_supervisors',
            ],
            'asst_commissioners': [
                'assistant_census_commissioners',
            ],
            'circle_officers': [
                'technical_staff_circle_officers',
            ],
            'deputy_commissioners': [
                'deputy_census_commissioners',
            ],
            'divisional_officer': [
                'technical_staff_divisional_census_officer',
            ],
            'enumerators_byoad': [
                'enumerators_who_used_smart_phones_byoad',
            ],
            'enumerators_capi': [
                'enumerators_who_used_tablet_computers_capi',
            ],
            'other_non_technical': [
                'other_non_technical_staff',
            ],
            'zonal_supervisors': [
                'technical_staff_zonal_supervisors_and_district'
                + '_statistical_branch_head',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'area_supervisors': '#38C5D0',
            'asst_commissioners': '#3840D0',
            'circle_officers': '#D0AF38',
            'deputy_commissioners': '#D05D38',
            'divisional_officer': '#D03899',
            'enumerators_byoad': '#D03847',
            'enumerators_capi': '#38D056',
            'other_non_technical': '#8238D0',
            'zonal_supervisors': '#6CD038',
        }
