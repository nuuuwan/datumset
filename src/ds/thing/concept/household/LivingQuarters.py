from ds.thing.concept.CategoryConcept import CategoryConcept


class LivingQuarters(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("housing_unit"),
            cls("collective_living_quarter"),
            cls("non_housing_unit"),
        ]
