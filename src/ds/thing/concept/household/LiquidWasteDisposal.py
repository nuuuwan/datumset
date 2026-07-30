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

    @classmethod
    def get_color_map(cls):
        return {
            "to_a_properly_closed_pit": "#D05D38",
            "open_pit": "#3840D0",
            "within_the_premises": "#6CD038",
            "connected_to_a_piped_sewer": "#D03899",
            "to_a_stream_or_spring_or_river_or_sea": "#38C5D0",
            "to_a_drain_on_road": "#D0AF38",
            "other": "#cccccc",
        }
