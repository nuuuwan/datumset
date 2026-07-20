# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusOfficer(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "deputy_census_commissioners",
            "assistant_census_commissioners",
            "technical_staff_zonal_supervisors_and_district_statistical_branch_head",  # noqa: E501
            "technical_staff_divisional_census_officer",
            "technical_staff_area_supervisors",
            # 6 - 9
            "technical_staff_circle_officers",
            "other_non_technical_staff",
            "enumerators_who_used_tablet_computers_capi",
            "enumerators_who_used_smart_phones_byoad",
        ]
