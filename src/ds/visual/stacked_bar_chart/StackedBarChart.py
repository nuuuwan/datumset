from ds.visual.stacked_bar_chart.StackedBarChartColorMixin import \
    StackedBarChartColorMixin
from ds.visual.stacked_bar_chart.StackedBarChartDataMixin import \
    StackedBarChartDataMixin
from ds.visual.stacked_bar_chart.StackedBarChartPlotMixin import \
    StackedBarChartPlotMixin
from ds.visual.visual.Visual import Visual


class StackedBarChart(
    StackedBarChartDataMixin,
    StackedBarChartColorMixin,
    StackedBarChartPlotMixin,
    Visual,
):

    def __init__(self, datumset):
        super().__init__(datumset)
        self.x_dim_key = self._get_varying_dim_keys()[-2]
        self.stack_dim_key = self._get_varying_dim_keys()[-1]
        self.y_cell_key = self._get_y_cell_key()
        self.display_datumsets = self._get_display_datumsets(
            {self.x_dim_key, self.stack_dim_key}
        )
        self.stack_values, self.stack_color_idx = self._init_category_colors(
            self.stack_dim_key
        )

    def _get_category_dim_key(self):
        return self.stack_dim_key

    def _excluded_dim_keys(self):
        return {self.x_dim_key, self.stack_dim_key}
