from ds.visual.shape_map.AbstractShapeMap import AbstractShapeMap
from ds.visual.square_map.SquareShapeMixin import SquareShapeMixin


class SquareMap(SquareShapeMixin, AbstractShapeMap):

    TILE_NOUN = "square"
