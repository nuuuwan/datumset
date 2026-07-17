from ds.thing.concept.CategoryConcept import CategoryConcept


class FloorType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Cement"),
            cls("Tile/granite/terrazo"),
            cls("Mud"),
            cls("Wood"),
            cls("Sand"),
            cls("Concrete"),
            cls("Other"),
        ]
