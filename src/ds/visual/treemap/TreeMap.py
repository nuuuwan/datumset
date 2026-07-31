from ds.visual.treemap.TreeMapDataMixin import TreeMapDataMixin
from ds.visual.treemap.TreeMapLabelMixin import TreeMapLabelMixin
from ds.visual.treemap.TreeMapPlotMixin import TreeMapPlotMixin
from ds.visual.visual.Visual import Visual


class TreeMap(TreeMapDataMixin, TreeMapLabelMixin, TreeMapPlotMixin, Visual):

    RECT_GAP = 0.008
    MIN_RECT_AREA_RATIO = 0.003
    MIN_LABEL_AREA_RATIO = 0.005

    def __init__(self, datumset):
        super().__init__(datumset)
        self.x_dim_key = self._get_varying_dim_keys()[-1]
        self.y_cell_key = self._get_y_cell_key()
        self.display_datumsets = self._get_display_datumsets({self.x_dim_key})
        self.x_values, self.x_color_idx = self._init_category_colors(
            self.x_dim_key
        )

    def _get_category_dim_key(self):
        return self.x_dim_key

    def _excluded_dim_keys(self):
        return {self.x_dim_key}
