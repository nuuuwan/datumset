from ds.thing.concept.CategoryConcept import CategoryConcept


class SolidWasteDisposal(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("CollectedByLocalAuthorities"),
            cls("OccupantsBurn"),
            cls("OccupantsBury"),
            cls("OccupantsCompostingSolidWaste"),
            cls(
                "OccupantsDisposeSolidWasteIntoRoad"
                "/river/canal/sea/creek/forestEtc"
            ),
            cls("Other"),
        ]
