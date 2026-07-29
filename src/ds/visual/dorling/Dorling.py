from ds.visual.dorling.DorlingDrawMixin import DorlingDrawMixin
from ds.visual.dorling.DorlingLabelMixin import DorlingLabelMixin
from ds.visual.dorling.DorlingLayoutMixin import DorlingLayoutMixin
from ds.visual.map_visual.MapVisual import MapVisual


class Dorling(
    DorlingLayoutMixin,
    DorlingDrawMixin,
    DorlingLabelMixin,
    MapVisual,
):
    pass
