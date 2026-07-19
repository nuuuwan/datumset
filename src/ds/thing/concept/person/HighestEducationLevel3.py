from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel3(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("NoSchooling"),
            cls("Passed1To5Years"),
            cls("Passed6To10Years"),
            cls("GCEOL"),
            cls("GCEAL"),
        ]
