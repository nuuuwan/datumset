from ds.thing.concept.CategoryConcept import CategoryConcept


class ElectionType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "parliamentary",
            "presidential",
            "local_government",
        ]
