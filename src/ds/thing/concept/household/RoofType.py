from ds.thing.concept.CategoryConcept import CategoryConcept


class RoofType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "tile",
            "asbestos",
            "concrete",
            "zink_aluminium_sheet",
            "metal_sheet",
            "cadjan_palmyrah_straw",
            "other",
            #
            "not_relevant",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "cadjan_or_palmyrah_or_straw": "cadjan_palmyrah_straw",
        }
