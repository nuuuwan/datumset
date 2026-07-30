import math


class PieChartLabelFitMixin:

    def _get_data_to_px(self, sub_ax):
        x0, _ = sub_ax.transData.transform((0, 0))
        x1, _ = sub_ax.transData.transform((1, 0))
        return abs(x1 - x0)

    def _set_slice_label_position(self, wedge, autotext, radius):
        mid_angle = math.radians((wedge.theta1 + wedge.theta2) / 2.0)
        label_radius = self.PIE_LABEL_RADIUS_FACTOR * radius
        autotext.set_position(
            (
                label_radius * math.cos(mid_angle),
                label_radius * math.sin(mid_angle),
            )
        )

    def _fit_single_slice_label(
        self,
        wedge,
        autotext,
        radius,
        data_to_px,
        renderer,
    ):
        self._set_slice_label_position(wedge, autotext, radius)
        label_radius = self.PIE_LABEL_RADIUS_FACTOR * radius
        theta_rad = math.radians(abs(wedge.theta2 - wedge.theta1))
        max_width_px = (
            theta_rad * label_radius * data_to_px * self.PIE_LABEL_BBOX_MARGIN
        )
        max_height_px = (radius - label_radius) * data_to_px * 0.9
        label_fontsize_cap = self._get_label_fontsize_cap(
            wedge,
            radius,
            data_to_px,
        )
        if label_fontsize_cap < self.MIN_PIE_LABEL_FONTSIZE:
            autotext.set_visible(False)
            return
        best_fontsize = min(
            label_fontsize_cap,
            self._get_best_fontsize(
                autotext,
                max_width_px,
                max_height_px,
                renderer,
            ),
        )
        if best_fontsize < self.MIN_PIE_LABEL_FONTSIZE:
            autotext.set_visible(False)
            return
        autotext.set_color(
            self._get_contrast_text_color(wedge.get_facecolor())
        )
        autotext.set_fontsize(best_fontsize)

    def _fit_slice_labels(self, sub_ax, wedges, autotexts, radius):
        renderer = self._get_renderer(sub_ax.figure)
        data_to_px = self._get_data_to_px(sub_ax)
        for wedge, autotext in zip(wedges, autotexts):
            self._fit_single_slice_label(
                wedge,
                autotext,
                radius,
                data_to_px,
                renderer,
            )
