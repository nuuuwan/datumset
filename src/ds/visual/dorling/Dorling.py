from ds.visual.dorling.DorlingDrawMixin import DorlingDrawMixin
from ds.visual.dorling.DorlingLabelMixin import DorlingLabelMixin
from ds.visual.dorling.DorlingLayoutMixin import DorlingLayoutMixin
from ds.visual.map.Map import Map


class Dorling(
    DorlingLayoutMixin,
    DorlingDrawMixin,
    DorlingLabelMixin,
    Map,
):

    def _use_count_weights(self):
        return self.y_cell_key == "Count"
