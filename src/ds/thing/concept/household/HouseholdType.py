from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdType(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 4
            "one_person",
            "nuclear",
            "extended",
            "composite",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "one_person": "#D05D38",
            "nuclear": "#3840D0",
            "extended": "#6CD038",
            "composite": "#D03899",
        }
