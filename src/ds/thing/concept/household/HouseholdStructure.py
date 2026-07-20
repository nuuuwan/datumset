from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdStructure(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "single_house_single_storeyed",
            "single_house_two_storeyed",
            "single_house_more_than_two_storeyed",
            "attached_house_or_annex",
            "flat",
            "condominium",
            "twin_house",
            "row_house_or_line_room",
            "hut_or_shanty",
            #
            "attached_house_1st_floor",
            "attached_house_2nd_floor",
            "attached_house_from_3_to_4_floors",
            "attached_house_from_5_to_10_floors",
            "attached_house_from_11_to_19_floors",
            "attached_house_from_20_floors_or_more",
            "other",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "single_house_single_floor": "single_house_single_storeyed",
            "single_house_double_floor": "single_house_two_storeyed",
            "single_house_more_than_2_floors": "single_house_more_than_two_storeyed",
        }
