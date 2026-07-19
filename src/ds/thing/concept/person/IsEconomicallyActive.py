from ds.thing.concept.CategoryConcept import CategoryConcept


class IsEconomicallyActive(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("employed"),
            cls("unemployed"),
            cls("economically_not_active"),
            cls("economically_active"),
            cls("economically_inactive"),
        ]
