from ds.thing.concept.CategoryConcept import CategoryConcept


class WaterSupplyAvailability(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("HouseholdsWithWaterSupplyThroughoutTheYear"),
            cls("HouseholdsWithNoWaterSupplyForAtLeastOneOneMonth"),
        ]
