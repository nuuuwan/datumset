from ds.thing.concept.CategoryConcept import CategoryConcept


class WallType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "brick",
            "cement_block_or_stone",
            "cabook",
            "soil_bricks",
            "mud",
            "cadjan_or_palmyrah",
            "plank_or_metal_sheet",
            "other",
        ]
