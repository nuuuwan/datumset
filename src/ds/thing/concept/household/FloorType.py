from ds.thing.concept.CategoryConcept import CategoryConcept


class FloorType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("cement"),
            cls("tile_or_granite_or_terrazo"),
            cls("mud"),
            cls("wood"),
            cls("sand"),
            cls("concrete"),
            cls("other"),
        ]
