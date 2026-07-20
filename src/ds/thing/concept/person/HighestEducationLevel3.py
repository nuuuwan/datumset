from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel3(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "no_schooling",
            "passed_1_5_years",
            "passed_6_10_years",
            "gce_ol",
            "gce_al",
        ]
