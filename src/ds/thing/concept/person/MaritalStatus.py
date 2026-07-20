from ds.thing.concept.CategoryConcept import CategoryConcept


class MaritalStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "never_married",
            "married_registered",
            "married_customary",
            "married",
            "widowed",
            "divorced",
            "legally_separated",
            "separated_not_legally",
            "not_stated",
        ]
