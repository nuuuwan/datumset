from ds.thing.concept.CategoryConcept import CategoryConcept


class WallType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Brick"),
            cls("CementBlock/stone"),
            cls("Cabook"),
            cls("SoilBricks"),
            cls("Mud"),
            cls("Cadjan/palmyrah"),
            cls("Plank/metalSheet"),
            cls("Other"),
        ]
