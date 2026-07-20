from ds.thing.concept.CategoryConcept import CategoryConcept


class OccupationStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "occupied",
            "vacant",
        ]
