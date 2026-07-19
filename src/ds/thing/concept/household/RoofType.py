from ds.thing.concept.CategoryConcept import CategoryConcept


class RoofType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("tile"),
            cls("asbestos"),
            cls("concrete"),
            cls("zink_aluminium_sheet"),
            cls("metal_sheet"),
            cls("cadjan_or_palmyrah_or_straw"),
            cls("other"),
        ]
