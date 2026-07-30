from ds.thing.concept.CategoryConcept import CategoryConcept


class SourceOfDrinkingWater(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "protected_well_within_premises",
            "protected_well_outside_premises",
            "unprotected_well",
            "tap_within_unit_main_line",
            "tap_within_premises_but_outside_unit_main_line",
            "tap_outside_premises_main_line",
            "rural_water_projects",
            "tube_well",
            "bowser",
            "river_or_tank_or_stream",
            "rain_water",
            "bottled_water",
            "other",
            #
            "pipe_borne_water",
            "ground_water",
            #
            "within_housing_unit",
            "within_premises",
            "outside_premises",
            #
            "protected_well",
            "semi_protected_well",
            "pipe_borne_water_national_water_supply_and_drainage_board",
            "pipe_borne_water_local_authority",
            "pipe_borne_water_community_based_organization",
            "pipe_borne_water_private_water_supply_project",
            "spring_or_fountain",
            "filter_water_r_o_plant",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "river_or_tank_or_stream": [
                "tank_river_stream",
                "tank_or_river_or_streams",
            ],
            "rain_water": ["rainwater"],
            "spring_or_fountain": ["spring_fountain"],
            "filter_water_r_o_plant": ["filter_ro"],
            "pipe_borne_water_national_water_supply_and_drainage_board": [
                "pipe_borne_nwsdb"
            ],
            "pipe_borne_water_local_authority": [
                "pipe_borne_local_authority"
            ],
            "pipe_borne_water_community_based_organization": [
                "pipe_borne_community"
            ],
            "pipe_borne_water_private_water_supply_project": [
                "pipe_borne_private"
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "protected_well_within_premises": "#D05D38",
            "protected_well_outside_premises": "#3840D0",
            "unprotected_well": "#6CD038",
            "tap_within_unit_main_line": "#D03899",
            "tap_within_premises_but_outside_unit_main_line": "#38C5D0",
            "tap_outside_premises_main_line": "#D0AF38",
            "rural_water_projects": "#8238D0",
            "tube_well": "#38D056",
            "bowser": "#D03847",
            "river_or_tank_or_stream": "#3873D0",
            "rain_water": "#9FD038",
            "bottled_water": "#D038CB",
            "other": "#cccccc",
            "pipe_borne_water": "#38D0A8",
            "ground_water": "#D07C38",
            "within_housing_unit": "#5038D0",
            "within_premises": "#4DD038",
            "outside_premises": "#D03879",
            "protected_well": "#38A6D0",
            "semi_protected_well": "#D0CE38",
            "pipe_borne_water_national_water_supply_and_drainage_board": "#A238D0",  # noqa: E501
            "pipe_borne_water_local_authority": "#38D076",
            "pipe_borne_water_community_based_organization": "#D04938",
            "pipe_borne_water_private_water_supply_project": "#3853D0",
            "spring_or_fountain": "#80D038",
            "filter_water_r_o_plant": "#D038AC",
        }
