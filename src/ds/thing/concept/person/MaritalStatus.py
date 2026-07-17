from ds.thing.concept.CategoryConcept import CategoryConcept


class MaritalStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("NeverMarried"),
            cls("Married((registered)"),
            cls("Married(customary)"),
            cls("Widowed"),
            cls("Divorced"),
            cls("LegallySeparated"),
            cls("Separated(notLegally)"),
            cls("NotStated"),
        ]
