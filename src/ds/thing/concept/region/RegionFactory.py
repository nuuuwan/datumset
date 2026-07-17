from functools import cache

from ds.thing.concept.region.District import District
from ds.thing.concept.region.DSD import DSD
from ds.thing.concept.region.ED import ED
from ds.thing.concept.region.LG import LG
from ds.thing.concept.region.PD import PD
from ds.thing.concept.region.Province import Province


class RegionFactory:

    @classmethod
    @cache
    def from_region_id_to_ec_regions(cls, region_id: str):
        assert region_id.startswith("EC-"), f"Invalid region_id: {region_id}"
        region_cls = {
            5: ED,
            6: PD,
        }.get(len(region_id))
        if not region_cls:
            raise ValueError(f"Unknown region_id: {region_id}")
        return region_cls

    @classmethod
    @cache
    def from_region_id_for_admin_region(cls, region_id: str):
        assert region_id.startswith("LK-"), f"Invalid region_id: {region_id}"
        region_cls = {4: Province, 5: District, 7: DSD}.get(len(region_id))
        if not region_cls:
            raise ValueError(f"Unknown region_id: {region_id}")
        return region_cls

    @classmethod
    @cache
    def from_region_id(cls, region_id: str):
        if region_id.startswith("LK-"):
            return cls.from_region_id_for_admin_region(region_id)
        if region_id.startswith("EC-"):
            return cls.from_region_id_to_ec_regions(region_id)
        if region_id.startswith("LG-"):
            return LG
        raise ValueError(f"Unknown region_id: {region_id}")

    @classmethod
    @cache
    def __class_getitem__(cls, class_name: str):
        entity_classes = [
            Province,
            District,
            DSD,
            ED,
            PD,
            LG,
        ]

        for entity_class in entity_classes:
            if entity_class.__name__ == class_name:
                return entity_class
        raise ValueError(f"[RegionFactory] Unknown class_name: {class_name}")
