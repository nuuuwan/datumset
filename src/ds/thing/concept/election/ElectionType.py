from ds.thing.concept.CategoryConcept import CategoryConcept


class ElectionType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("parliamentary"),
            cls("presidential"),
            cls("local_government"),
        ]
