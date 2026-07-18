from ds.thing.concept.CategoryConcept import CategoryConcept


class MaritalStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("NeverMarried"),
            cls("MarriedRegistered"),
            cls("MarriedCustomary"),
            cls("Married"),
            cls("Widowed"),
            cls("Divorced"),
            cls("LegallySeparated"),
            cls("SeparatedNotLegally"),
            cls("NotStated"),
        ]
