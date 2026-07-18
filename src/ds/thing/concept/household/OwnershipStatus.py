from ds.thing.concept.CategoryConcept import CategoryConcept


class OwnershipStatus(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("OwnedByAHouseholdMember"),
            cls("RentOrLeaseGovernmentOwned"),
            cls("RentOrLeasePrivatelyOwned"),
            cls("OccupiedFreeOfRent"),
            cls("Encroached"),
            cls("Other"),
        ]
