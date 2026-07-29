class StackedBarChartPlotMixin:

    def _get_y_limit(self):
        y_max = 0.0
        for sub_datumset in self.display_datumsets:
            x_labels, _, data = self._get_data(sub_datumset)
            totals = self._get_totals(x_labels, data)
            if totals:
                y_max = max(y_max, max(totals))
        return self._get_y_axis_limit(y_max)

    def _plot_stack_for_x(
        self,
        sub_ax,
        x_value,
        x_label,
        stack_labels,
        data,
        total,
    ):
        bottom = 0.0
        sorted_stack_labels = self._get_sorted_stack_labels_for_x(
            stack_labels,
            data,
            x_label,
        )
        for stack_label in sorted_stack_labels:
            value = data[stack_label].get(x_label, 0.0)
            color = self.stack_color_idx[stack_label]
            bars = sub_ax.bar(
                [x_value],
                [value],
                bottom=[bottom],
                color=color,
            )
            self._add_stacked_bar_percentages(
                sub_ax,
                bars,
                [value],
                [total],
            )
            bottom += value

    def _plot_subfigure(self, sub_ax, sub_datumset, y_limit):
        x_labels, stack_labels, data = self._get_data(sub_datumset)
        x_values = list(range(len(x_labels)))
        totals = self._get_totals(x_labels, data)
        sub_ax.set_xlim(-0.5, len(x_labels) - 0.5)
        sub_ax.set_ylim(0, y_limit)
        for x_value, x_label, total in zip(x_values, x_labels, totals):
            self._plot_stack_for_x(
                sub_ax,
                x_value,
                x_label,
                stack_labels,
                data,
                total,
            )
        self._add_bar_totals(sub_ax, x_values, totals, y_limit)
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
        self._add_color_legend(
            fig,
            self.stack_color_idx,
            self.stack_dim_key,
            self._get_category_win_counts(),
        )
        self._hide_empty_axes(axes, n_datumsets)
