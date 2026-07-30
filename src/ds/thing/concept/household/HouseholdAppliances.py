from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdAppliances(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            "radio",
            "television",
            "fixed_line_telephone",
            "smart_mobile_phone",
            "normal_mobile_phone",
            "desktop_computer",
            "laptop_computer",
            "tablet_computer",
            "internet_facilities",
            "bicycle",
            "motorcycle_or_scooter",
            "three_wheeler",
            "other",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "radio": "#D05D38",
            "television": "#3840D0",
            "fixed_line_telephone": "#6CD038",
            "smart_mobile_phone": "#D03899",
            "normal_mobile_phone": "#38C5D0",
            "desktop_computer": "#D0AF38",
            "laptop_computer": "#8238D0",
            "tablet_computer": "#38D056",
            "internet_facilities": "#D03847",
            "bicycle": "#3873D0",
            "motorcycle_or_scooter": "#9FD038",
            "three_wheeler": "#D038CB",
            "other": "#cccccc",
        }
