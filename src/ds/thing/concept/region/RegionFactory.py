from ds.thing.concept.region.District import District


class RegionFactory:

    @classmethod
    def from_region_id_for_admin_region(cls, region_id: str):
        len_region_id = len(region_id)
        region_cls = {
            5: District,
        }.get(len_region_id)
        if not region_cls:
            raise ValueError(f"Unknown region_id: {region_id}")
        return region_cls

    @classmethod
    def from_region_id(cls, region_id: str):
        if region_id.startswith("LK-"):
            return cls.from_region_id_for_admin_region(region_id)
        raise ValueError(f"Unknown region_id: {region_id}")
