from ds.query.Query import Query
from ds.visual.map_visual.MapVisualColorMixin import MapVisualColorMixin
from ds.visual.map_visual.MapVisualGdfMixin import MapVisualGdfMixin
from ds.visual.map_visual.MapVisualGeoMixin import MapVisualGeoMixin
from ds.visual.map_visual.MapVisualLabelMixin import MapVisualLabelMixin
from ds.visual.map_visual.MapVisualPercentMixin import MapVisualPercentMixin
from ds.visual.map_visual.MapVisualPlotMixin import MapVisualPlotMixin
from ds.visual.visual.Visual import Visual


class MapVisual(
    MapVisualGeoMixin,
    MapVisualGdfMixin,
    MapVisualColorMixin,
    MapVisualLabelMixin,
    MapVisualPercentMixin,
    MapVisualPlotMixin,
    Visual,
):

    REGION_EDGE_COLOR = "#888888"
    REGION_EDGE_LINEWIDTH = 0.3
    CELL_TOP = "Top"

    def __init__(self, datumset):
        super().__init__(datumset)
        self.region_dim_key = self._get_region_dim_key()
        self.y_cell_key = self._get_y_cell_key()
        self.region_color_dim_key = self._get_region_color_dim_key()
        self.display_datumsets = self._get_display_datumsets(
            self._excluded_split_dim_keys()
        )

    def _is_top(self):
        query_str = getattr(self.datumset, "_query_str", None)
        if query_str is None:
            return False
        return Query(query_str).cell_part == self.CELL_TOP

    def _get_region_color_dim_key(self):
        if not self._is_top():
            return None
        return self._get_dim_labels()[-1]

    def _excluded_split_dim_keys(self):
        keys = {self.region_dim_key}
        if self.region_color_dim_key is not None:
            keys.add(self.region_color_dim_key)
        return keys

    def _excluded_dim_keys(self):
        return self._excluded_split_dim_keys() | {self.y_cell_key}
