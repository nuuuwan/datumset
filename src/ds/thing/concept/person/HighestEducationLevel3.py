from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel3(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("no_schooling"),
            cls("passed_1_5_years"),
            cls("passed_6_10_years"),
            cls("gce_ol"),
            cls("gce_al"),
        ]
