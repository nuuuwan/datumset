from ds.thing.concept.CategoryConcept import CategoryConcept


class ToiletFacilities(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "water_seal_and_connected_to_a_piped_sewer_system",
            "water_seal_and_connected_to_a_septic_tank",
            "pour_flush_toilet_not_water_seal",
            "direct_pit",
            "other",
            "not_using_a_toilet",
            #
            "not_using_a_toilet_use_jungle_beach_and_open_ground",
            "no_toilet_but_sharing_with_another_housing_unit_or_units",
            "common_or_public_toilet",
            "within_premises_sharing_with_another_household",
            "within_premises_exclusively_for_the_household",
            "within_the_housing_unit_sharing_with_another_household",
            "within_the_housing_unit_exclusively_for_the_household",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "within_the_housing_unit_exclusively_for_the_household": [
                "within_unit_exclusive"
            ],
            "within_the_housing_unit_sharing_with_another_household": [
                "within_unit_shared"
            ],
            "within_premises_exclusively_for_the_household": [
                "within_premises_exclusive"
            ],
            "within_premises_sharing_with_another_household": [
                "within_premises_shared"
            ],
            "no_toilet_but_sharing_with_another_housing_unit_or_units": [
                "no_toilet_sharing"
            ],
            "common_or_public_toilet": ["common_public"],
            "not_using_a_toilet": ["none"],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "water_seal_and_connected_to_a_piped_sewer_system": "#D05D38",
            "water_seal_and_connected_to_a_septic_tank": "#3840D0",
            "pour_flush_toilet_not_water_seal": "#6CD038",
            "direct_pit": "#D03899",
            "other": "#cccccc",
            "not_using_a_toilet": "#cccccc",
            "not_using_a_toilet_use_jungle_beach_and_open_ground": "#38C5D0",
            "no_toilet_but_sharing_with_another_housing_unit_or_units": "#D0AF38",  # noqa: E501
            "common_or_public_toilet": "#8238D0",
            "within_premises_sharing_with_another_household": "#38D056",
            "within_premises_exclusively_for_the_household": "#D03847",
            "within_the_housing_unit_sharing_with_another_household": "#3873D0",
            "within_the_housing_unit_exclusively_for_the_household": "#9FD038",
        }
