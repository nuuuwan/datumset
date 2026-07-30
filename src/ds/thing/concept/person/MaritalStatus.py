from ds.thing.concept.CategoryConcept import CategoryConcept


class MaritalStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "never_married",
            "married_registered",
            "married_customary",
            "married",
            "widowed",
            "divorced",
            "legally_separated",
            "separated_not_legal",
            "not_stated",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "separated_not_legal": [
                "separated_not_legally",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "never_married": "#D05D38",
            "married_registered": "#3840D0",
            "married_customary": "#6CD038",
            "married": "#D03899",
            "widowed": "#38C5D0",
            "divorced": "#D0AF38",
            "legally_separated": "#8238D0",
            "separated_not_legal": "#38D056",
            "not_stated": "#cccccc",
        }
