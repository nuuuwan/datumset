import matplotlib.pyplot as plt

from ds.visual.Visual import Visual


class BarChart(Visual):

    def __init__(self, datumset, x_dim_key=None, y_cell_key=None):
        super().__init__(datumset)
        query = datumset[0].query
        self.x_dim_key = x_dim_key or query.dim_labels[0]
        self.y_cell_key = y_cell_key or query.cell_labels[0]
        self.display_datumsets = self._get_display_datumsets({self.x_dim_key})
        self.x_values = self._get_unique_dim_values(self.x_dim_key)
        cmap = plt.get_cmap("tab20")
        self.x_color_idx = {
            x_value: cmap(i % cmap.N)
            for i, x_value in enumerate(self.x_values)
        }

    def _get_xy(self, datumset):
        x_labels = []
        y_values = []
        for datum in datumset:
            x_labels.append(datum.dim_idx[self.x_dim_key].get_value())
            y_values.append(
                float(datum.cell_idx[self.y_cell_key].get_value())
            )
        return x_labels, y_values

    def _excluded_dim_keys(self):
        return {self.x_dim_key}

    def _build_title(self):
        return f"{self.y_cell_key} by {self.x_dim_key}"

    def _get_title_text(self):
        entity = self.datumset[0].entity_class.__name__
        return f"{entity} {self.y_cell_key} by {self.x_dim_key}"

    def _get_y_limit(self):
        y_max = 0.0
        for sub_datumset in self.display_datumsets:
            _, y_values = self._get_xy(sub_datumset)
            if y_values:
                y_max = max(y_max, max(y_values))
        return 1.0 if y_max <= 0 else y_max * 1.1

    def _plot_subfigure(self, sub_ax, sub_datumset, y_limit):
        x_labels, y_values = self._get_xy(sub_datumset)
        colors = [self.x_color_idx[x_label] for x_label in x_labels]
        sub_ax.bar(range(len(x_labels)), y_values, color=colors)
        sub_ax.set_ylabel(self.y_cell_key)
        sub_ax.set_ylim(0, y_limit)
        self._format_humanized_y_axis(sub_ax)
        sub_ax.set_xticks([])
        sub_ax.set_box_aspect(1)
        sub_ax.set_title(
            self._get_subfigure_title(sub_datumset, {self.x_dim_key}),
            fontsize=7,
            pad=3,
        )

    def _plot(self, fig, ax):
        n_datumsets = len(self.display_datumsets)
        axes = self._get_square_axes(fig, ax, n_datumsets)
        y_limit = self._get_y_limit()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset, y_limit)
        self._add_color_legend(fig, self.x_color_idx, self.x_dim_key)
        self._hide_empty_axes(axes, n_datumsets)
