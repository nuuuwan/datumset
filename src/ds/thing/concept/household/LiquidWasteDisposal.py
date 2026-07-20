from ds.thing.concept.CategoryConcept import CategoryConcept


class LiquidWasteDisposal(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "to_a_properly_closed_pit",
            "open_pit",
            "within_the_premises",
            "connected_to_a_piped_sewer",
            "to_a_stream_or_spring_or_river_or_sea",
            "to_a_drain_on_road",
            "other",
        ]
