# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusOfficer(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("deputy_census_commissioners"),
            cls("assistant_census_commissioners"),
            cls(
                "technical_staff_zonal_supervisors_and_district_statistical_branch_head"
            ),
            cls("technical_staff_divisional_census_officer"),
            cls("technical_staff_area_supervisors"),
            # 6 - 9
            cls("technical_staff_circle_officers"),
            cls("other_non_technical_staff"),
            cls("enumerators_who_used_tablet_computers_capi"),
            cls("enumerators_who_used_smart_phones_byoad"),
        ]
