from ds.visual.map.Map import Map
from ds.visual.shape_map.ShapeMapAssignMixin import ShapeMapAssignMixin
from ds.visual.shape_map.ShapeMapBoundaryMixin import ShapeMapBoundaryMixin
from ds.visual.shape_map.ShapeMapCountMixin import ShapeMapCountMixin
from ds.visual.shape_map.ShapeMapDrawMixin import ShapeMapDrawMixin
from ds.visual.shape_map.ShapeMapGridMixin import ShapeMapGridMixin
from ds.visual.shape_map.ShapeMapLabelMixin import ShapeMapLabelMixin
from ds.visual.shape_map.ShapeMapScaleMixin import ShapeMapScaleMixin


class AbstractShapeMap(
    ShapeMapCountMixin,
    ShapeMapGridMixin,
    ShapeMapAssignMixin,
    ShapeMapDrawMixin,
    ShapeMapBoundaryMixin,
    ShapeMapLabelMixin,
    ShapeMapScaleMixin,
    Map,
):
    pass
