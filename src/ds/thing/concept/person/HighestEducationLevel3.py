from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel3(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("no_schooling"),
            cls("passed15_years"),
            cls("passed610_years"),
            cls("gce_ol"),
            cls("gce_al"),
        ]
