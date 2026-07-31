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
        self.x_dim_key = self._get_varying_dim_keys()[-1]
        self.y_cell_key = self._get_y_cell_key()
        self.display_datumsets = self._get_display_datumsets({self.x_dim_key})
        self.display_datumsets = self._get_sorted_display_datumsets()
        self.x_values, self.x_color_idx = self._init_category_colors(
            self.x_dim_key
        )

    def _get_sorted_display_datumsets(self):
        if len(self.display_datumsets) <= 1:
            return self.display_datumsets
        return sorted(
            self.display_datumsets,
            key=self._get_sub_datumset_total,
            reverse=True,
        )

    def _get_category_dim_key(self):
        return self.x_dim_key

    def _excluded_dim_keys(self):
        return {self.x_dim_key}
