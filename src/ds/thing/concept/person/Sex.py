from ds.thing.concept.CategoryConcept import CategoryConcept


class Sex(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("male"),
            cls("female"),
        ]
