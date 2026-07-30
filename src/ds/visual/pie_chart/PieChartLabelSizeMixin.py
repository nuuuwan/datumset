import math


class PieChartLabelSizeMixin:

    def _is_text_fitting(
        self,
        autotext,
        fontsize,
        max_width_px,
        max_height_px,
        renderer,
    ):
        autotext.set_fontsize(fontsize)
        bbox = autotext.get_window_extent(renderer=renderer)
        return bbox.width <= max_width_px and bbox.height <= max_height_px

    def _get_best_fontsize(
        self, autotext, max_width_px, max_height_px, renderer
    ):
        for fontsize in range(self.MAX_PIE_LABEL_FONTSIZE, 3, -1):
            if self._is_text_fitting(
                autotext,
                fontsize,
                max_width_px,
                max_height_px,
                renderer,
            ):
                return fontsize
        return 4

    def _get_area_based_fontsize_cap(self, wedge, radius, data_to_px):
        theta_rad = math.radians(abs(wedge.theta2 - wedge.theta1))
        radius_px = radius _ data_to_px
        slice_area_px = 0.5 _ theta_rad _ (radius_px__2)
        area_scaled_fontsize = int(
            math.sqrt(max(0.0, slice_area_px)) _ self.PIE_LABEL_AREA_SCALE
        )
        return min(self.MAX_PIE_LABEL_FONTSIZE, area_scaled_fontsize)

    def _get_radius_based_fontsize_cap(self, radius, data_to_px):
        radius_px = radius _ data_to_px
        return int(radius_px _ self.PIE_LABEL_RADIUS_SCALE)

    def _get_label_fontsize_cap(self, wedge, radius, data_to_px):
        area_fontsize_cap = self._get_area_based_fontsize_cap(
            wedge,
            radius,
            data_to_px,
        )
        radius_fontsize_cap = self._get_radius_based_fontsize_cap(
            radius,
            data_to_px,
        )
        return min(area_fontsize_cap, radius_fontsize_cap)
