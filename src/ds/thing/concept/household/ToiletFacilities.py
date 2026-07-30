from ds.thing.concept.CategoryConcept import CategoryConcept


class ToiletFacilities(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "water_seal_piped",
            "water_seal_septic",
            "pour_flush",
            "direct_pit",
            "other",
            "not_using_a_toilet",
            "no_toilet_open",
            "no_toilet_sharing",
            "common_public",
            "premises_shared",
            "premises_exclusive",
            "housing_unit_shared",
            "housing_unit_private",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "common_public": [
                "common_or_public_toilet",
            ],
            "housing_unit_private": [
                "within_unit_exclusive",
                "within_the_housing_unit_exclusively_for_the_household",
            ],
            "housing_unit_shared": [
                "within_unit_shared",
                "within_the_housing_unit_sharing_with_another_household",
            ],
            "no_toilet_open": [
                "not_using_a_toilet_use_jungle_beach_and_open_ground",
            ],
            "no_toilet_sharing": [
                "no_toilet_but_sharing_with_another_housing_unit_or_units",
            ],
            "not_using_a_toilet": [
                "none",
            ],
            "pour_flush": [
                "pour_flush_toilet_not_water_seal",
            ],
            "premises_exclusive": [
                "within_premises_exclusive",
                "within_premises_exclusively_for_the_household",
            ],
            "premises_shared": [
                "within_premises_shared",
                "within_premises_sharing_with_another_household",
            ],
            "water_seal_piped": [
                "water_seal_and_connected_to_a_piped_sewer_system",
            ],
            "water_seal_septic": [
                "water_seal_and_connected_to_a_septic_tank",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "water_seal_piped": "#D05D38",
            "water_seal_septic": "#3840D0",
            "pour_flush": "#6CD038",
            "direct_pit": "#D03899",
            "other": "#cccccc",
            "not_using_a_toilet": "#cccccc",
            "no_toilet_open": "#38C5D0",
            "no_toilet_sharing": "#D0AF38",
            "common_public": "#8238D0",
            "premises_shared": "#38D056",
            "premises_exclusive": "#D03847",
            "housing_unit_shared": "#3873D0",
            "housing_unit_private": "#9FD038",
        }
