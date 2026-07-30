from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationLifetimeDirection(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 2
            "in_migrants",
            "out_migrants",
        ]
