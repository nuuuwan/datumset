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
            "single_house_more_than_2_floors": "single_house_more"
            + "_than_two_storeyed",
        }

    @classmethod
    def get_color_map(cls):
        return {
            "single_house_single_storeyed": "#D05D38",
            "single_house_two_storeyed": "#3840D0",
            "single_house_more_than_two_storeyed": "#6CD038",
            "attached_house_or_annex": "#D03899",
            "flat": "#38C5D0",
            "condominium": "#D0AF38",
            "twin_house": "#8238D0",
            "row_house_or_line_room": "#38D056",
            "hut_or_shanty": "#D03847",
            "attached_house_1st_floor": "#3873D0",
            "attached_house_2nd_floor": "#9FD038",
            "attached_house_from_3_to_4_floors": "#D038CB",
            "attached_house_from_5_to_10_floors": "#38D0A8",
            "attached_house_from_11_to_19_floors": "#D07C38",
            "attached_house_from_20_floors_or_more": "#5038D0",
            "other": "#cccccc",
        }
