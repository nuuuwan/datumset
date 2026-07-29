from utils_future import Percent


class PieChartPlotMixin:

    def _plot_subfigure(
        self,
        sub_ax,
        sub_datumset,
        max_total,
        n_datumsets,
    ):
        x_labels, y_values = self._get_category_cell_xy(
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
            autopct=lambda value: Percent(value / 100.0).humanize,
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
