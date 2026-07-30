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
            "tank_river_stream": "river_or_tank_or_stream",
            "tank_or_river_or_streams": "river_or_tank_or_stream",
            "rainwater": "rain_water",
            "spring_fountain": "spring_or_fountain",
            "filter_ro": "filter_water_r_o_plant",
            "pipe_borne_nwsdb": "pipe_borne_water_national_water"
            + "_supply_and_drainage_board",
            "pipe_borne_local_authority": "pipe_borne_water_local_authority",
            "pipe_borne_community": "pipe_borne_water_community"
            + "_based_organization",
            "pipe_borne_private": "pipe_borne_water_private"
            + "_water_supply_project",
        }
