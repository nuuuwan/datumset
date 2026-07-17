from ds.thing.concept.CategoryConcept import CategoryConcept


class OwnershipStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("OwnedByAHouseholdMember"),
            cls("Rent/leaseGovernmentOwned"),
            cls("Rent/leasePrivatelyOwned"),
            cls("OccupiedFreeOfRent"),
            cls("Encroached"),
            cls("Other"),
        ]
