from ds.thing.concept.CategoryConcept import CategoryConcept


class ToiletFacilities(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("WaterSealAndConnectedToAPipedSewerSystem"),
            cls("WaterSealAndConnectedToASepticTank"),
            cls("PourFlushToiletNotWaterSeal"),
            cls("DirectPit"),
            cls("Other"),
            cls("NotUsingAToilet"),
        ]
