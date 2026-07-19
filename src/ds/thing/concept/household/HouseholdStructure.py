from ds.thing.concept.CategoryConcept import CategoryConcept


class HouseholdStructure(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("single_house_single_floor"),
            cls("single_house_double_floor"),
            cls("single_house_more_than_2_floors"),
            cls("attached_house_or_annex"),
            cls("flat"),
            cls("condominium"),
            cls("twin_house"),
            cls("row_house_or_line_room"),
            cls("hut_or_shanty"),
        ]
