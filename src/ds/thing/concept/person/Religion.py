from ds.thing.concept.CategoryConcept import CategoryConcept


class Religion(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("buddhist"),
            cls("hindu"),
            cls("islam"),
            cls("roman_catholic"),
            cls("other_christian"),
            cls("other"),
        ]
