from ds.visual.pie_chart.PieChartLabelFitMixin import PieChartLabelFitMixin
from ds.visual.pie_chart.PieChartLabelSizeMixin import PieChartLabelSizeMixin
from ds.visual.pie_chart.PieChartPlotMixin import PieChartPlotMixin
from ds.visual.pie_chart.PieChartSliceMixin import PieChartSliceMixin
from ds.visual.visual.Visual import Visual


class PieChart(
    PieChartLabelSizeMixin,
    PieChartLabelFitMixin,
    PieChartSliceMixin,
    PieChartPlotMixin,
    Visual,
):

    MIN_PIE_LABEL_FONTSIZE = 6
    MAX_PIE_LABEL_FONTSIZE = 20
    PIE_LABEL_RADIUS_FACTOR = 0.58
    PIE_LABEL_BBOX_MARGIN = 0.8
    PIE_LABEL_AREA_SCALE = 0.12
    PIE_LABEL_RADIUS_SCALE = 0.10

    def __init__(self, datumset):
        super().__init__(datumset)
        self.x_dim_key = self._get_first_varying_non_region_dim_key()
        self.y_cell_key = self._get_y_cell_key()
        self.display_datumsets = self._get_display_datumsets({self.x_dim_key})
        self.x_values, self.x_color_idx = self._init_category_colors(
            self.x_dim_key
        )

    def _get_category_dim_key(self):
        return self.x_dim_key

    def _excluded_dim_keys(self):
        return {self.x_dim_key}
