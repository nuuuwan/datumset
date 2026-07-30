from ds.thing.concept.CategoryConcept import CategoryConcept


class ElectionType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "parliamentary",
            "presidential",
            "local_government",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "parliamentary": "#D05D38",
            "presidential": "#3840D0",
            "local_government": "#6CD038",
        }
