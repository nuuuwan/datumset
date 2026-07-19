from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("primary"),
            cls("secondary"),
            cls("gce_ordinary_level"),
            cls("gce_advanced_level"),
            cls("degree_and_above"),
            cls("no_schooling"),
        ]
