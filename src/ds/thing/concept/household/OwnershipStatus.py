from ds.thing.concept.CategoryConcept import CategoryConcept


class OwnershipStatus(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "owned_by_a_household_member",
            "rent_or_lease_government_owned",
            "rent_or_lease_privately_owned",
            "occupied_free_of_rent",
            "encroached",
            "other",
            #
            "rent_or_lease_free_of_rent",
        ]

    @classmethod
    def get_color_map(cls):
        return {
            "owned_by_a_household_member": "#D05D38",
            "rent_or_lease_government_owned": "#3840D0",
            "rent_or_lease_privately_owned": "#6CD038",
            "occupied_free_of_rent": "#D03899",
            "encroached": "#38C5D0",
            "other": "#cccccc",
            "rent_or_lease_free_of_rent": "#D0AF38",
        }
