from ds.visual.hex_map.HexMapAssignMixin import HexMapAssignMixin
from ds.visual.hex_map.HexMapBoundaryMixin import HexMapBoundaryMixin
from ds.visual.hex_map.HexMapCountMixin import HexMapCountMixin
from ds.visual.hex_map.HexMapDrawMixin import HexMapDrawMixin
from ds.visual.hex_map.HexMapGridMixin import HexMapGridMixin
from ds.visual.hex_map.HexMapLabelMixin import HexMapLabelMixin
from ds.visual.map_visual.MapVisual import MapVisual


class HexMap(
    HexMapCountMixin,
    HexMapGridMixin,
    HexMapAssignMixin,
    HexMapDrawMixin,
    HexMapBoundaryMixin,
    HexMapLabelMixin,
    MapVisual,
):
    pass
