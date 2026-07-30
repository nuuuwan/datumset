from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdStructure(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "single_storeyed",
            "two_storeyed",
            "single_house_multi",
            "attached_house",
            "flat",
            "condominium",
            "twin_house",
            "row_house",
            "hut_or_shanty",
            "attached_1st_floor",
            "attached_2nd_floor",
            "attached_3_4_floors",
            "attached_5_to_10",
            "attached_11_to_19",
            "attached_20_plus",
            "other",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "attached_11_to_19": [
                "attached_house_from_11_to_19_floors",
            ],
            "attached_1st_floor": [
                "attached_house_1st_floor",
            ],
            "attached_20_plus": [
                "attached_house_from_20_floors_or_more",
            ],
            "attached_2nd_floor": [
                "attached_house_2nd_floor",
            ],
            "attached_3_4_floors": [
                "attached_house_from_3_to_4_floors",
            ],
            "attached_5_to_10": [
                "attached_house_from_5_to_10_floors",
            ],
            "attached_house": [
                "attached_house_or_annex",
            ],
            "row_house": [
                "row_house_or_line_room",
            ],
            "single_house_multi": [
                "single_house_more_than_2_floors",
                "single_house_more_than_two_storeyed",
            ],
            "single_storeyed": [
                "single_house_single_floor",
                "single_house_single_storeyed",
            ],
            "two_storeyed": [
                "single_house_double_floor",
                "single_house_two_storeyed",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "single_storeyed": "#D05D38",
            "two_storeyed": "#3840D0",
            "single_house_multi": "#6CD038",
            "attached_house": "#D03899",
            "flat": "#38C5D0",
            "condominium": "#D0AF38",
            "twin_house": "#8238D0",
            "row_house": "#38D056",
            "hut_or_shanty": "#D03847",
            "attached_1st_floor": "#3873D0",
            "attached_2nd_floor": "#9FD038",
            "attached_3_4_floors": "#D038CB",
            "attached_5_to_10": "#38D0A8",
            "attached_11_to_19": "#D07C38",
            "attached_20_plus": "#5038D0",
            "other": "#cccccc",
        }
