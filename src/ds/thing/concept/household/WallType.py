from ds.thing.concept.CategoryConcept import CategoryConcept


class WallType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Brick"),
            cls("CementBlockOrStone"),
            cls("Cabook"),
            cls("SoilBricks"),
            cls("Mud"),
            cls("CadjanOrPalmyrah"),
            cls("PlankOrMetalSheet"),
            cls("Other"),
        ]
