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

    @classmethod
    def get_color_map(cls):
        return {
            "buddhist": "#FFBE29",
            "hindu": "#DF7500",
            "islam": "#005F56",
            "roman_catholic": "#8e44ad",
            "other_christian": "#2980b9",
            "other": "#cccccc",
        }
