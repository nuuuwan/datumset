from ds.thing.concept.CategoryConcept import CategoryConcept


class Gender(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Male"),
            cls("Female"),
        ]
