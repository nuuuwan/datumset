from ds.thing.concept.CategoryConcept import CategoryConcept


class FloorType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "cement",
            "tile_or_granite_or_terrazo",
            "mud",
            "wood",
            "sand",
            "concrete",
            "other",
            #
            "terrazzo_tile_granite_wood_finished",
            "not_relevant",
        ]
