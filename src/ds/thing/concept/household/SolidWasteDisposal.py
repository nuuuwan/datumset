from ds.thing.concept.CategoryConcept import CategoryConcept


class SolidWasteDisposal(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "collected_by_local_authorities",
            "occupants_burn",
            "occupants_bury",
            "occupants_composting_solid_waste",
            "occupants_dispose_solid_waste_into_road_or_river_or_canal_or_sea_or_creek_or_forest_etc",  # noqa: E501
            "other",
        ]
