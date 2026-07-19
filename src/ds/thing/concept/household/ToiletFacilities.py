from ds.thing.concept.CategoryConcept import CategoryConcept


class ToiletFacilities(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("water_seal_and_connected_to_a_piped_sewer_system"),
            cls("water_seal_and_connected_to_a_septic_tank"),
            cls("pour_flush_toilet_not_water_seal"),
            cls("direct_pit"),
            cls("other"),
            cls("not_using_a_toilet"),
        ]
