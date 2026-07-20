from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel3(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("no_schooling"),
            cls("passed1_5_years"),
            cls("passed6_10_years"),
            cls("gce_ol"),
            cls("gce_al"),
        ]
