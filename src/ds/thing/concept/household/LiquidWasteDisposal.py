from ds.thing.concept.CategoryConcept import CategoryConcept


class LiquidWasteDisposal(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("to_a_properly_closed_pit"),
            cls("open_pit"),
            cls("within_the_premises"),
            cls("connected_to_a_piped_sewer"),
            cls("to_a_stream_or_spring_or_river_or_sea"),
            cls("to_a_drain_on_road"),
            cls("other"),
        ]
