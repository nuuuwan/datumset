import math

from ds.visual.Visual import Visual


class PieChart(Visual):

    def __init__(
        self,
        datumset,
        x_dim_key=None,
        y_cell_key=None,
    ):
        super().__init__(datumset)
        self.x_dim_key = self._resolve_dim_key(x_dim_key, 2)
        self.y_cell_key = self._resolve_cell_key(y_cell_key)
        self.display_datumsets = self._get_display_datumsets({self.x_dim_key})
        self.x_values, self.x_color_idx = self._init_dim_colors(
            self.x_dim_key
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
        for fontsize in range(20, 3, -1):
            if self._is_text_fitting(
                autotext,
                fontsize,
                max_width_px,
                max_height_px,
                renderer,
            ):
                return fontsize
        return 4

    def _fit_slice_labels(self, sub_ax, wedges, autotexts):
        fig = sub_ax.figure
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        data_to_px = self._get_data_to_px(sub_ax)
        label_radius = 0.6
        radial_margin = 0.9
        for wedge, autotext in zip(wedges, autotexts):
            theta_rad = math.radians(abs(wedge.theta2 - wedge.theta1))
            max_width_px = theta_rad * label_radius * data_to_px * 0.9
            max_height_px = (1 - label_radius) * data_to_px * radial_margin
            best_fontsize = self._get_best_fontsize(
                autotext,
                max_width_px,
                max_height_px,
                renderer,
            )
            autotext.set_fontsize(best_fontsize)

    def _build_autopct(self, y_values):
        total = sum(y_values)

        def _autopct(pct):
            value = total * pct / 100.0
            value_text = self._format_humanized_value(value, None)
            if pct > 0.5:
                pct_text = f"{pct:.0f}%"
            else:
                pct_text = "<0.5%"
            return f"{value_text} ({pct_text})"

        return _autopct

    def _plot_subfigure(self, sub_ax, sub_datumset):
        x_labels, y_values = self._get_dim_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
        )
        colors = [self.x_color_idx[x_label] for x_label in x_labels]
        wedges, _, autotexts = sub_ax.pie(
            y_values,
            colors=colors,
            autopct=self._build_autopct(y_values),
            pctdistance=0.6,
            textprops={"color": "white"},
        )
        self._fit_slice_labels(sub_ax, wedges, autotexts)
        self._set_square_subfigure_title(sub_ax, sub_datumset)

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset)
        self._add_color_legend(fig, self.x_color_idx, self.x_dim_key)
        self._hide_empty_axes(axes, n_datumsets)
