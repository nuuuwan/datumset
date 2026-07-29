from ds.visual.hex_map.HexShapeMixin import HexShapeMixin
from ds.visual.shape_map.AbstractShapeMap import AbstractShapeMap


class HexMap(HexShapeMixin, AbstractShapeMap):

    TILE_NOUN = "hexagon"
