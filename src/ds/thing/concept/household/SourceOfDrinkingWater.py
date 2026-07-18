from ds.thing.concept.CategoryConcept import CategoryConcept


class SourceOfDrinkingWater(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("ProtectedWellWithinPremises"),
            cls("ProtectedWellOutsidePremises"),
            cls("UnprotectedWell"),
            cls("TapWithinUnitMainLine"),
            cls("TapWithinPremisesButOutsideUnitMainLine"),
            cls("TapOutsidePremisesMainLine"),
            cls("RuralWaterProjects"),
            cls("TubeWell"),
            cls("Bowser"),
            cls("RiverOrTankOrStream"),
            cls("RainWater"),
            cls("BottledWater"),
            cls("Other"),
        ]
