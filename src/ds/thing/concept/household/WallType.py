from ds.thing.concept.CategoryConcept import CategoryConcept


class WallType(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("brick"),
            cls("cement_block_or_stone"),
            cls("cabook"),
            cls("soil_bricks"),
            cls("mud"),
            cls("cadjan_or_palmyrah"),
            cls("plank_or_metal_sheet"),
            cls("other"),
        ]
