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
            "spring_fountain",
            "pipe_borne_nwsdb",
            "pipe_borne_local_authority",
            "pipe_borne_community",
            "pipe_borne_private",
            "tank_river_stream",
            "filter_ro",
        ]
