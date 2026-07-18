from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroup(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("LessThan10"),
            cls("1019"),
            cls("2029"),
            cls("3039"),
            cls("4049"),
            cls("5059"),
            cls("6069"),
            cls("7079"),
            cls("8089"),
            cls("90AndAbove"),
        ]
