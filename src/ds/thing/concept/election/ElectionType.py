from ds.thing.concept.CategoryConcept import CategoryConcept


class ElectionType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Parliamentary"),
            cls("Presidential"),
            cls("LocalGovernment"),
        ]
