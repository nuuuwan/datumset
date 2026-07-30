from ds.thing.concept.region.Country import Country
from ds.thing.concept.region.DSD import DSD
from ds.thing.concept.region.District import District
from ds.thing.concept.region.ED import ED
from ds.thing.concept.region.GND import GND
from ds.thing.concept.region.PD import PD
from ds.thing.concept.region.Province import Province


class EntityClassListRegionMixin:
    ENTITY_CLASS_LIST = [
        Country,
        DSD,
        District,
        ED,
        GND,
        #
        PD,
        Province,
    ]
