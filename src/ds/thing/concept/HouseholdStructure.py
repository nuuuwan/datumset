from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdStructure(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("SingleHouseSingleFloor"),
            cls("SingleHouseDoubleFloor"),
            cls("SingleHouseMoreThan2Floors"),
            cls("AttachedHouse/annex"),
            cls("Flat"),
            cls("Condominium"),
            cls("TwinHouse"),
            cls("RowHouse/LineRoom"),
            cls("Hut/shanty"),
        ]
