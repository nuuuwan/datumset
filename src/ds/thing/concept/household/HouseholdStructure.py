from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdStructure(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("SingleHouseSingleFloor"),
            cls("SingleHouseDoubleFloor"),
            cls("SingleHouseMoreThan2Floors"),
            cls("AttachedHouseOrAnnex"),
            cls("Flat"),
            cls("Condominium"),
            cls("TwinHouse"),
            cls("RowHouseOrLineRoom"),
            cls("HutOrShanty"),
        ]
