import math

from ds.visual.Visual import Visual


class PieChart(Visual):

    MIN_PIE_LABEL_FONTSIZE = 6
    MAX_PIE_LABEL_FONTSIZE = 20
    PIE_LABEL_RADIUS_FACTOR = 0.58
    PIE_LABEL_BBOX_MARGIN = 0.8
    PIE_LABEL_AREA_SCALE = 0.12
    PIE_LABEL_RADIUS_SCALE = 0.10

    def __init__(
        self,
        datumset,
    ):
        super().__init__(datumset)
        self.x_dim_key, self.y_cell_key = self.params
        self.display_datumsets = self._get_display_datumsets({self.x_dim_key})
        self.x_values, self.x_color_idx = self._init_dim_colors(
            self.x_dim_key
        )

    def _get_params(self):
        return (
            self._get_first_varying_non_region_dim_key(),
            self._get_y_cell_key(),
        )

    def _excluded_dim_keys(self):
        return {self.x_dim_key}

    def _build_title(self):
        return self._build_dim_title(self.y_cell_key, self.x_dim_key)

    def _get_title_text(self):
        return self._build_entity_dim_title(
            self.y_cell_key,
            self.x_dim_key,
            relation="share by",
        )

    def _get_data_to_px(self, sub_ax):
        x0, _ = sub_ax.transData.transform((0, 0))
        x1, _ = sub_ax.transData.transform((1, 0))
        return abs(x1 - x0)

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

    def _set_slice_label_position(self, wedge, autotext, radius):
        mid_angle = math.radians((wedge.theta1 + wedge.theta2) / 2.0)
        label_radius = self.PIE_LABEL_RADIUS_FACTOR * radius
        autotext.set_position(
            (
                label_radius * math.cos(mid_angle),
                label_radius * math.sin(mid_angle),
            )
        )

    def _get_area_based_fontsize_cap(self, wedge, radius, data_to_px):
        theta_rad = math.radians(abs(wedge.theta2 - wedge.theta1))
        radius_px = radius * data_to_px
        slice_area_px = 0.5 * theta_rad * (radius_px**2)
        area_scaled_fontsize = int(
            math.sqrt(max(0.0, slice_area_px)) * self.PIE_LABEL_AREA_SCALE
        )
        return min(self.MAX_PIE_LABEL_FONTSIZE, area_scaled_fontsize)

    def _get_radius_based_fontsize_cap(self, radius, data_to_px):
        radius_px = radius * data_to_px
        return int(radius_px * self.PIE_LABEL_RADIUS_SCALE)

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
        fig = sub_ax.figure
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        data_to_px = self._get_data_to_px(sub_ax)
        for wedge, autotext in zip(wedges, autotexts):
            self._fit_single_slice_label(
                wedge,
                autotext,
                radius,
                data_to_px,
                renderer,
            )

    def _build_autopct(self):
        def _autopct(pct):
            if pct > 0.5:
                return f"{pct:.0f}%"
            return "<0.5%"

        return _autopct

    def _get_total_value_text(self, y_values):
        total = sum(y_values)
        return self._format_humanized_value(total, None)

    def _get_pie_radius(self, total, max_total, n_datumsets):
        if n_datumsets <= 1 or max_total <= 0:
            return 1.0
        scale = math.sqrt(total / max_total) if total > 0 else 0.0
        return max(0.3, scale)

    def _set_subfigure_title_with_total(self, sub_ax, sub_datumset, y_values):
        base_title = self._get_subfigure_title(
            sub_datumset,
            self._excluded_dim_keys(),
        )
        total_text = self._get_total_value_text(y_values)
        sub_ax.set_title(
            f"{base_title}\n{total_text}",
            fontsize=7,
            pad=3,
        )

    def _get_sub_datumset_total(self, sub_datumset):
        _, y_values = self._get_dim_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
        )
        return sum(y_values)

    def _get_sorted_slice_data(self, x_labels, y_values):
        combined = sorted(
            zip(x_labels, y_values),
            key=lambda item: item[1],
            reverse=True,
        )
        if not combined:
            return [], []
        sorted_x_labels, sorted_y_values = zip(*combined)
        return list(sorted_x_labels), list(sorted_y_values)

    def _plot_subfigure(
        self,
        sub_ax,
        sub_datumset,
        max_total,
        n_datumsets,
    ):
        x_labels, y_values = self._get_dim_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
        )
        x_labels, y_values = self._get_sorted_slice_data(x_labels, y_values)
        total = sum(y_values)
        radius = self._get_pie_radius(total, max_total, n_datumsets)
        colors = [self.x_color_idx[x_label] for x_label in x_labels]
        wedges, _, autotexts = sub_ax.pie(
            y_values,
            colors=colors,
            autopct=self._build_autopct(),
            pctdistance=self.PIE_LABEL_RADIUS_FACTOR,
            radius=radius,
            startangle=90,
            counterclock=False,
            textprops={"color": self.CONTRAST_DARK_TEXT_COLOR},
        )
        self._fit_slice_labels(sub_ax, wedges, autotexts, radius)
        self._set_square_subfigure_title(sub_ax, sub_datumset)
        self._set_subfigure_title_with_total(sub_ax, sub_datumset, y_values)

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        totals = [
            self._get_sub_datumset_total(sub_datumset)
            for sub_datumset in self.display_datumsets
        ]
        max_total = max(totals) if totals else 0.0
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(
                sub_ax,
                sub_datumset,
                max_total,
                n_datumsets,
            )
        self._add_color_legend(fig, self.x_color_idx, self.x_dim_key)
        self._hide_empty_axes(axes, n_datumsets)
