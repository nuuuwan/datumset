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
            "cadjan_or_palmyrah_or_straw",
            "other",
        ]
