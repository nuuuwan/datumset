from ds.thing.concept.CategoryConcept import CategoryConcept


class OccupationStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("occupied"),
            cls("vacant"),
        ]
