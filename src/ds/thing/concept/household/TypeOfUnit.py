from ds.thing.concept.CategoryConcept import CategoryConcept


class TypeOfUnit(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "permanent",
            "not_permanent",
            "semi_permanent",
            "improvised",
            "unclassified",
        ]
