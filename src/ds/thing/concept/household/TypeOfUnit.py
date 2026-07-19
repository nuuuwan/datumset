from ds.thing.concept.CategoryConcept import CategoryConcept


class TypeOfUnit(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("permanent"),
            cls("not_permanent"),
            cls("semi_permanent"),
            cls("improvised"),
            cls("unclassified"),
        ]
