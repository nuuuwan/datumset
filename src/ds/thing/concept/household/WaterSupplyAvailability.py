from ds.thing.concept.CategoryConcept import CategoryConcept


class WaterSupplyAvailability(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("households_with_water_supply_throughout_the_year"),
            cls("households_with_no_water_suppply_for_at_least_one_month"),
        ]
