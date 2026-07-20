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
            "water_seal_and_connected_to_a_piped_sewer_system",
            "no_toilet_but_sharing_with_another_housing_unit_or_units",
            "water_seal_and_connected_to_a_piped_sewer_system",
            "common_or_public_toilet",
            "within_premises_sharing_with_another_household",
            "within_premises_exclusively_for_the_household",
            "within_the_housing_unit_sharing_with_another_household",
            "within_the_housing_unit_exclusively_for_the_household",
            "water_seal_and_connected_to_a_piped_sewer_system",
            #
            "within_unit_exclusive",
            "within_unit_shared",
            "within_premises_exclusive",
            "within_premises_shared",
            "no_toilet_sharing",
            "common_public",
            "none",
        ]
