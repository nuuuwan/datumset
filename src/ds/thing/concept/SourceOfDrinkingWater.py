from ds.thing.concept.CategoryConcept import CategoryConcept


class SourceOfDrinkingWater(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("ProtectedWellWithinPremises"),
            cls("ProtectedWellOutsidePremises"),
            cls("UnprotectedWell"),
            cls("TapWithinUnit(mainLine)"),
            cls("TapWithinPremisesButOutsideUnit(mainLine)"),
            cls("TapOutsidePremises(mainLine)"),
            cls("RuralWaterProjects"),
            cls("TubeWell"),
            cls("Bowser"),
            cls("River/tank/stream"),
            cls("RainWater"),
            cls("BottledWater"),
            cls("Other"),
        ]
