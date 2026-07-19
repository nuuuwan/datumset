from ds.thing.concept.CategoryConcept import CategoryConcept


class SourceOfDrinkingWater(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("protected_well_within_premises"),
            cls("protected_well_outside_premises"),
            cls("unprotected_well"),
            cls("tap_within_unit_main_line"),
            cls("tap_within_premises_but_outside_unit_main_line"),
            cls("tap_outside_premises_main_line"),
            cls("rural_water_projects"),
            cls("tube_well"),
            cls("bowser"),
            cls("river_or_tank_or_stream"),
            cls("rain_water"),
            cls("bottled_water"),
            cls("other"),
        ]
