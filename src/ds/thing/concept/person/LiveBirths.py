from ds.thing.concept.CategoryConcept import CategoryConcept


class LiveBirths(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "0",
            "1",
            "2",
            "3",
            "4",
            # 6 - 8
            "5",
            "6",
            "7_or_more",
        ]

    @classmethod
    def map_alias(cls) -> dict:
        return {
            "7_or_more": ["7_plus"],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "0": "#D05D38",
            "1": "#3840D0",
            "2": "#6CD038",
            "3": "#D03899",
            "4": "#38C5D0",
            "5": "#D0AF38",
            "6": "#8238D0",
            "7_or_more": "#38D056",
        }
