from ds.thing.concept.CategoryConcept import CategoryConcept


class SolidWasteDisposal(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("collected_by_local_authorities"),
            cls("occupants_burn"),
            cls("occupants_bury"),
            cls("occupants_composting_solid_waste"),
            cls(
                "occupants_dispose_solid_waste_into_road_or_river_or_canal_or_sea_or_creek_or_forest_etc"  # noqa: E501
            ),
            cls("other"),
        ]
