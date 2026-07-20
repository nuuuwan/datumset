from ds.thing.concept.CategoryConcept import CategoryConcept


class Gender(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "male",
            "female",
        ]
