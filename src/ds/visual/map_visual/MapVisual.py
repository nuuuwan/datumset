from ds.visual.map_visual.MapVisualColorMixin import MapVisualColorMixin
from ds.visual.map_visual.MapVisualGeoMixin import MapVisualGeoMixin
from ds.visual.map_visual.MapVisualLabelMixin import MapVisualLabelMixin
from ds.visual.map_visual.MapVisualPlotMixin import MapVisualPlotMixin
from ds.visual.visual.Visual import Visual


class MapVisual(
    MapVisualGeoMixin,
    MapVisualColorMixin,
    MapVisualLabelMixin,
    MapVisualPlotMixin,
    Visual,
):

    REGION_EDGE_COLOR = "#888888"
    REGION_EDGE_LINEWIDTH = 0.3

    def __init__(self, datumset):
        super().__init__(datumset)
        self.region_dim_key = self._get_region_dim_key()
        self.y_cell_key = self._get_y_cell_key()
        self.display_datumsets = self._get_display_datumsets(
            {self.region_dim_key}
        )

    def _excluded_dim_keys(self):
        return {self.region_dim_key, self.y_cell_key}
