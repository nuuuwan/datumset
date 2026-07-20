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
    def list(cls):
        return [cls(value) for value in cls.valid_values()]
