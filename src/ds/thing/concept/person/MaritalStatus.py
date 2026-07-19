from ds.thing.concept.CategoryConcept import CategoryConcept


class MaritalStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("never_married"),
            cls("married_registered"),
            cls("married_customary"),
            cls("married"),
            cls("widowed"),
            cls("divorced"),
            cls("legally_separated"),
            cls("separated_not_legally"),
            cls("not_stated"),
        ]
