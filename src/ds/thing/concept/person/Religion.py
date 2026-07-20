from ds.thing.concept.CategoryConcept import CategoryConcept


class Religion(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "buddhist",
            "hindu",
            "islam",
            "roman_catholic",
            "other_christian",
            "other",
        ]
