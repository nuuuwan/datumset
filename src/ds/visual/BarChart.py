from ds.visual.visual.Visual import Visual


class BarChart(Visual):

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

    def _get_x_label_colors(self, sub_datumset, x_labels):
        labels, values = self._get_category_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
        )
        value_by_x = dict(zip(labels, values))
        max_value = max(values) if values else 1.0
        return [
            self._get_share_shaded_color(
                self.x_color_idx[x_label],
                value_by_x.get(x_label, 0.0) / max_value,
            )
            for x_label in x_labels
        ]

    def _excluded_dim_keys(self):
        return {self.x_dim_key}

    def _get_y_limit(self):
        y_max = 0.0
        for sub_datumset in self.display_datumsets:
            _, y_values = self._get_category_cell_xy(
                sub_datumset,
                self.x_dim_key,
                self.y_cell_key,
            )
            if y_values:
                y_max = max(y_max, max(y_values))
        return self._get_y_axis_limit(y_max)

    def _plot_subfigure(self, sub_ax, sub_datumset, y_limit):
        order = self._get_category_value_order(
            self.x_dim_key,
            self.y_cell_key,
        )
        x_labels, y_values = self._get_ordered_category_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
            order,
        )
        x_values = list(range(len(x_labels)))
        colors = [self.x_color_idx[x_label] for x_label in x_labels]
        sub_ax.bar(x_values, y_values, color=colors)
        self._add_bar_totals(sub_ax, x_values, y_values, y_limit)
        self._style_value_axis_subfigure(
            sub_ax,
            self.y_cell_key,
            y_limit,
            sub_datumset,
            x_labels,
        )

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        y_limit = self._get_y_limit()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset, y_limit)
        self._add_color_legend(fig, self.x_color_idx, self.x_dim_key)
        self._hide_empty_axes(axes, n_datumsets)
