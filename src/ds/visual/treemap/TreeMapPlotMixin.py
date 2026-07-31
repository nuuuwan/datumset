from matplotlib.patches import Rectangle


class TreeMapPlotMixin:

    def _plot_subfigure(self, sub_ax, sub_datumset):
        x_labels, y_values, total = self._get_tree_map_data(sub_datumset)
        rectangles = self._get_rectangles(y_values, total)
        for x_label, value, (x, y, width, height, _) in zip(
            x_labels,
            y_values,
            rectangles,
        ):
            rect = Rectangle(
                (x, y),
                width,
                height,
                facecolor=self.x_color_idx[x_label],
                edgecolor=self.SUBTITLE_COLOR,
                linewidth=0.5,
            )
            sub_ax.add_patch(rect)
            self._add_rect_label(sub_ax, rect, x_label, value, total)
        self._style_tree_map_subfigure(sub_ax, sub_datumset)

    def _style_tree_map_subfigure(self, sub_ax, sub_datumset):
        sub_ax.set_xlim(0, 1)
        sub_ax.set_ylim(0, 1)
        sub_ax.set_box_aspect(1)
        sub_ax.set_xticks([])
        sub_ax.set_yticks([])
        for spine in sub_ax.spines.values():
            spine.set_visible(False)
        self._set_subfigure_title(sub_ax, sub_datumset)

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset)
        self._add_color_legend(
            fig,
            self.x_color_idx,
            self.x_dim_key,
            self._get_category_counts(),
        )
        self._hide_empty_axes(axes, n_datumsets)

    def _get_category_counts(self):
        if len(self.display_datumsets) <= 1:
            return None
        counts = {}
        for x_value in self.x_values:
            counts[x_value] = counts.get(x_value, 0) + 1
        return counts
