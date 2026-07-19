from ds.thing.concept.CategoryConcept import CategoryConcept


class OwnershipStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("owned_by_a_household_member"),
            cls("rent_or_lease_government_owned"),
            cls("rent_or_lease_privately_owned"),
            cls("occupied_free_of_rent"),
            cls("encroached"),
            cls("other"),
        ]
