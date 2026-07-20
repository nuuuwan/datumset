from ds.thing.concept.CategoryConcept import CategoryConcept


class LivingQuarters(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "housing_unit",
            "collective_living_quarter",
            "non_housing_unit",
        ]
