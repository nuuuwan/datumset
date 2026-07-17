from ds.thing.concept.CategoryConcept import CategoryConcept


class Religion(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Buddhist"),
            cls("Hindu"),
            cls("Islam"),
            cls("RomanCatholic"),
            cls("OtherChristian"),
            cls("Other"),
        ]
