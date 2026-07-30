class MekkoPlotMixin:

    def _plot_segment(
        self,
        sub_ax,
        geometry,
        stack_label,
        value,
        total,
        bottom,
    ):
        left, width = geometry
        height = self._get_segment_height(value, total)
        color = self.stack_color_idx[stack_label]
        bars = sub_ax.bar(
            [left + width / 2.0],
            [height],
            bottom=[bottom],
            width=width,
            color=color,
        )
        self._segment_labels.append((bars[0], value))
        return height

    def _get_global_sorted_stack_labels(self, stack_labels, data):
        return sorted(
            stack_labels,
            key=lambda stack_label: sum(data[stack_label].values()),
            reverse=True,
        )

    def _plot_bar(self, sub_ax, geometry, x_label, stack_labels, data, total):
        bottom = 0.0
        sorted_stack_labels = self._get_global_sorted_stack_labels(
            stack_labels,
            data,
        )
        for stack_label in sorted_stack_labels:
            value = data[stack_label].get(x_label, 0.0)
            bottom += self._plot_segment(
                sub_ax,
                geometry,
                stack_label,
                value,
                total,
                bottom,
            )

    def _add_segment_labels(self, sub_ax):
        for rect, value in self._segment_labels:
            label = self._format_humanized_value(float(value), None)
            self._add_fitted_label_in_rect(sub_ax, rect, label)

    def _plot_subfigure(self, sub_ax, sub_datumset):
        x_labels, stack_labels, data = self._get_data(sub_datumset)
        totals = self._get_totals(x_labels, data)
        geometries = self._get_bar_geometry(totals)
        self._segment_labels = []
        for geometry, x_label, total in zip(geometries, x_labels, totals):
            self._plot_bar(
                sub_ax,
                geometry,
                x_label,
                stack_labels,
                data,
                total,
            )
        self._style_mekko_subfigure(
            sub_ax,
            geometries,
            x_labels,
            totals,
            sub_datumset,
        )
        self._add_segment_labels(sub_ax)
