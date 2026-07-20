from ds.thing.concept.CategoryConcept import CategoryConcept


class ToiletFacilities(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("water_seal_and_connected_to_a_piped_sewer_system"),
            cls("water_seal_and_connected_to_a_septic_tank"),
            cls("pour_flush_toilet_not_water_seal"),
            cls("direct_pit"),
            cls("other"),
            cls("not_using_a_toilet"),
            #
            cls("not_using_a_toilet_use_jungle_beach_and_open_ground"),
            cls("water_seal_and_connected_to_a_piped_sewer_system"),
            cls("no_toilet_but_sharing_with_another_housing_unit_or_units"),
            cls("water_seal_and_connected_to_a_piped_sewer_system"),
            cls("common_or_public_toilet"),
            cls("within_premises_sharing_with_another_household"),
            cls("within_premises_exclusively_for_the_household"),
            cls("within_the_housing_unit_sharing_with_another_household"),
            cls("within_the_housing_unit_exclusively_for_the_household"),
            cls("water_seal_and_connected_to_a_piped_sewer_system"),
        ]
