from ds.thing.concept.CategoryConcept import CategoryConcept


class RoofType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Tile"),
            cls("Asbestos"),
            cls("Concrete"),
            cls("ZinkAluminiumSheet"),
            cls("MetalSheet"),
            cls("Cadjan/palmyrah/straw"),
            cls("Other"),
        ]
