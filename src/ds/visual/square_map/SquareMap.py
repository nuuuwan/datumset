from ds.visual.hex_map.HexMap import HexMap
from ds.visual.square_map.SquareMapBoundaryMixin import (
    SquareMapBoundaryMixin,
)
from ds.visual.square_map.SquareMapDrawMixin import SquareMapDrawMixin
from ds.visual.square_map.SquareMapGridMixin import SquareMapGridMixin
from ds.visual.square_map.SquareMapLabelMixin import SquareMapLabelMixin


class SquareMap(
    SquareMapGridMixin,
    SquareMapDrawMixin,
    SquareMapBoundaryMixin,
    SquareMapLabelMixin,
    HexMap,
):

    TILE_NOUN = "square"
