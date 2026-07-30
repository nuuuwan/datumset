from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationLifetimeDirection(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 2
            "in_migrants",
            "out_migrants",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "in_migrants": "#D05D38",
            "out_migrants": "#3840D0",
        }
