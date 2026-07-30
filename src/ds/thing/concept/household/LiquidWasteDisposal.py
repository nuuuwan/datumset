from ds.thing.concept.CategoryConcept import CategoryConcept


class LiquidWasteDisposal(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "closed_pit",
            "open_pit",
            "within_the_premises",
            "piped_sewer",
            "natural_water",
            "to_a_drain_on_road",
            "other",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "closed_pit": [
                "to_a_properly_closed_pit",
            ],
            "natural_water": [
                "to_a_stream_or_spring_or_river_or_sea",
            ],
            "piped_sewer": [
                "connected_to_a_piped_sewer",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "closed_pit": "#D05D38",
            "open_pit": "#3840D0",
            "within_the_premises": "#6CD038",
            "piped_sewer": "#D03899",
            "natural_water": "#38C5D0",
            "to_a_drain_on_road": "#D0AF38",
            "other": "#cccccc",
        }
