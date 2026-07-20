from ds.thing.concept.CategoryConcept import CategoryConcept


class Sex(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "male",
            "female",
            "both_sexes",
        ]
