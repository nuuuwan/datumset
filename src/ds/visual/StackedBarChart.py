from collections import defaultdict

import matplotlib.pyplot as plt

from ds.visual.Visual import Visual


class StackedBarChart(Visual):

    def __init__(
        self,
        datumset,
        x_dim_key=None,
        stack_dim_key=None,
        y_cell_key=None,
    ):
        super().__init__(datumset, x_dim_key, stack_dim_key, y_cell_key)
        query = datumset[0].query
        self.x_dim_key = x_dim_key or query.dim_labels[1]
        self.stack_dim_key = stack_dim_key or query.dim_labels[2]
        self.y_cell_key = y_cell_key or query.cell_labels[0]
        self.display_datumsets = self._get_display_datumsets(
            {self.x_dim_key, self.stack_dim_key}
        )
        self.stack_values = self._get_unique_dim_values(self.stack_dim_key)
        cmap = plt.get_cmap("tab20")
        self.stack_color_idx = {
            stack_value: cmap(i % cmap.N)
            for i, stack_value in enumerate(self.stack_values)
        }

    def _get_data(self, datumset):
        x_labels, stack_labels = [], []
        data = defaultdict(dict)
        for datum in datumset:
            x = datum.dim_idx[self.x_dim_key].get_value()
            s = datum.dim_idx[self.stack_dim_key].get_value()
            v = float(datum.cell_idx[self.y_cell_key].get_value())
            if x not in x_labels:
                x_labels.append(x)
            if s not in stack_labels:
                stack_labels.append(s)
            data[s][x] = v
        return x_labels, stack_labels, data

    def _excluded_dim_keys(self):
        return {self.x_dim_key, self.stack_dim_key}

    def _build_title(self):
        return (
            f"{self.y_cell_key} by {self.x_dim_key}"
            f", stacked by {self.stack_dim_key}"
        )

    def _get_title_text(self):
        entity = self.datumset[0].entity_class.__name__
        return (
            f"{entity} {self.y_cell_key} by {self.x_dim_key}, "
            f"stacked by {self.stack_dim_key}"
        )

    def _get_y_limit(self):
        y_max = 0.0
        for sub_datumset in self.display_datumsets:
            x_labels, _, data = self._get_data(sub_datumset)
            totals = []
            for x_label in x_labels:
                total = sum(
                    data[stack_label].get(x_label, 0.0)
                    for stack_label in data.keys()
                )
                totals.append(total)
            if totals:
                y_max = max(y_max, max(totals))
        return 1.0 if y_max <= 0 else y_max * 1.1

    def _plot_subfigure(self, sub_ax, sub_datumset, y_limit):
        x_labels, stack_labels, data = self._get_data(sub_datumset)
        bottoms = [0.0] * len(x_labels)
        for stack_label in stack_labels:
            values = [
                data[stack_label].get(x_label, 0.0) for x_label in x_labels
            ]
            color = self.stack_color_idx[stack_label]
            sub_ax.bar(
                range(len(x_labels)),
                values,
                bottom=bottoms,
                color=color,
            )
            bottoms = [b + v for b, v in zip(bottoms, values)]
        sub_ax.set_ylabel(self.y_cell_key)
        sub_ax.set_ylim(0, y_limit)
        self._format_humanized_y_axis(sub_ax)
        sub_ax.set_xticks([])
        sub_ax.set_box_aspect(1)
        sub_ax.set_title(
            self._get_subfigure_title(
                sub_datumset,
                {self.x_dim_key, self.stack_dim_key},
            ),
            fontsize=7,
            pad=3,
        )

    def _plot(self, fig, ax):
        n_datumsets = len(self.display_datumsets)
        axes = self._get_square_axes(fig, ax, n_datumsets)
        y_limit = self._get_y_limit()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset, y_limit)
        self._add_color_legend(fig, self.stack_color_idx, self.stack_dim_key)
        self._hide_empty_axes(axes, n_datumsets)
