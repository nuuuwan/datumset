from ds.thing.concept.CategoryConcept import CategoryConcept


class WaterSupplyAvailability(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "households_with_water_supply_throughout_the_year",
            "households_with_no_water_suppply_for_at_least_one_month",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "households_with_water_supply_throughout_the_year": "#D05D38",
            "households_with_no_water_suppply_for_at_least_one_month": "#3840D0",  # noqa: E501
        }
