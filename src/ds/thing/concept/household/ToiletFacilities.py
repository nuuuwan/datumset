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
            "within_unit_exclusive": "within_the_housing_unit"
            + "_exclusively_for_the_household",
            "within_unit_shared": "within_the_housing_unit"
            + "_sharing_with_another_household",
            "within_premises_exclusive": "within_premises"
            + "_exclusively_for_the_household",
            "within_premises_shared": "within_premises"
            + "_sharing_with_another_household",
            "no_toilet_sharing": "no_toilet_but_sharing"
            + "_with_another_housing_unit_or_units",
            "common_public": "common_or_public_toilet",
            "none": "not_using_a_toilet",
        }
