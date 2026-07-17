from ds.thing.concept.CategoryConcept import CategoryConcept


class TypeOfUnit(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Permanent"),
            cls("SemiPermanent"),
            cls("Improvised"),
            cls("Unclassified"),
        ]
