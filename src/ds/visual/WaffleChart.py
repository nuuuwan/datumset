import matplotlib.pyplot as plt

from ds.visual.visual.Visual import Visual


class WaffleChart(Visual):

    GRID_SIZE = 10
    FIGSIZE = (7, 7)

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

    def _excluded_dim_keys(self):
        return {self.x_dim_key}

    @staticmethod
    def _get_category_counts(x_labels, y_values):
        totals = {}
        for x_label, y_value in zip(x_labels, y_values):
            totals[x_label] = totals.get(x_label, 0.0) + y_value
        return totals

    def _get_sorted_category_data(self, sub_datumset):
        x_labels, y_values = self._get_category_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
        )
        totals = self._get_category_counts(x_labels, y_values)
        order = self._get_category_value_order(
            self.x_dim_key, self.y_cell_key
        )
        sorted_x = self._apply_x_order(list(totals.keys()), order)
        return sorted_x, [totals[x] for x in sorted_x]

    def _get_fill_plan(self, x_labels, y_values):
        total = sum(y_values)
        if total <= 0:
            return []
        n_cells = self.GRID_SIZE * self.GRID_SIZE
        counts = []
        remainders = []
        for y_value in y_values:
            exact = y_value / total * n_cells
            counts.append(int(exact))
            remainders.append(exact - counts[-1])
        while sum(counts) < n_cells:
            idx = max(range(len(remainders)), key=lambda i: remainders[i])
            counts[idx] += 1
            remainders[idx] = 0
        plan = []
        for x_label, count in zip(x_labels, counts):
            plan.extend([x_label] * count)
        return plan

    def _plot_subfigure(self, sub_ax, sub_datumset):
        x_labels, y_values = self._get_sorted_category_data(sub_datumset)
        plan = self._get_fill_plan(x_labels, y_values)
        cell_index = 0
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                x_label = plan[cell_index]
                color = self.x_color_idx[x_label]
                sub_ax.add_patch(
                    plt.Rectangle(
                        (col, row),
                        1,
                        1,
                        facecolor=color,
                        edgecolor="#ffffff",
                        linewidth=0.5,
                    )
                )
                cell_index += 1
        sub_ax.set_xlim(0, self.GRID_SIZE)
        sub_ax.set_ylim(0, self.GRID_SIZE)
        sub_ax.set_aspect("equal")
        sub_ax.set_axis_off()
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
