class MarimekkoPlotMixin:

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
        self._register_hover(sub_ax, bars[0], stack_label, value)
        self._add_stacked_bar_percentages(sub_ax, bars, [value], [total])
        return height

    def _plot_bar(self, sub_ax, geometry, x_label, stack_labels, data, total):
        bottom = 0.0
        sorted_stack_labels = self._get_sorted_stack_labels_for_x(
            stack_labels,
            data,
            x_label,
        )
        for stack_label in sorted_stack_labels:
            value = data[stack_label].get(x_label, 0.0)
            if value <= 0:
                continue
            bottom += self._plot_segment(
                sub_ax,
                geometry,
                stack_label,
                value,
                total,
                bottom,
            )

    def _plot_subfigure(self, sub_ax, sub_datumset):
        x_labels, stack_labels, data = self._get_data(sub_datumset)
        totals = self._get_totals(x_labels, data)
        geometries = self._get_bar_geometry(totals)
        self._add_hover_annotation(sub_ax)
        for geometry, x_label, total in zip(geometries, x_labels, totals):
            if total <= 0 or geometry[1] <= 0:
                continue
            self._plot_bar(
                sub_ax,
                geometry,
                x_label,
                stack_labels,
                data,
                total,
            )
        self._style_marimekko_subfigure(
            sub_ax,
            geometries,
            x_labels,
            totals,
            sub_datumset,
        )
