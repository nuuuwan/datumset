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
