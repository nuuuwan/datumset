from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel3(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("NoSchooling"),
            cls("Passed15Years"),
            cls("Passed610Years"),
            cls("GceOl"),
            cls("GceAl"),
        ]
