from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdStructure(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "single_house_single_floor",
            "single_house_double_floor",
            "single_house_more_than_2_floors",
            "attached_house_or_annex",
            "flat",
            "condominium",
            "twin_house",
            "row_house_or_line_room",
            "hut_or_shanty",
        ]
