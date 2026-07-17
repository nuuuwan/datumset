from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Primary"),
            cls("Secondary"),
            cls("GceOrdinaryLevel"),
            cls("GceAdvancedLevel"),
            cls("DegreeAndAbove"),
            cls("NoSchooling"),
        ]
