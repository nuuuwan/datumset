import math

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from ds.visual.Visual import Visual


class BarChart(Visual):

    def __init__(self, datumset, x_dim_key=None, y_cell_key=None):
        super().__init__(datumset)
        query = datumset[0].query
        self.x_dim_key = x_dim_key or query.dim_labels[0]
        self.y_cell_key = y_cell_key or query.cell_labels[0]
        split_dims = [dim for dim in query.dim_labels if dim != self.x_dim_key]
        self.display_datumsets = datumset.split(*split_dims)
        self.x_values = []
        for datum in datumset:
            x_value = datum.dim_idx[self.x_dim_key].get_value()
            if x_value not in self.x_values:
                self.x_values.append(x_value)
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
            y_values.append(float(datum.cell_idx[self.y_cell_key].get_value()))
        return x_labels, y_values

    def _excluded_dim_keys(self):
        return {self.x_dim_key}

    def _build_title(self):
        return f"{self.y_cell_key} by {self.x_dim_key}"

    def _get_title_text(self):
        entity = self.datumset[0].entity_class.__name__
        return f"{entity} {self.y_cell_key} by {self.x_dim_key}"

    def _get_subfigure_title(self, datumset):
        constant_parts = []
        first_datum = datumset[0]
        for dim_key in first_datum.query.dim_labels:
            if dim_key == self.x_dim_key:
                continue
            first_value = first_datum.dim_idx[dim_key].get_value()
            if all(
                datum.dim_idx[dim_key].get_value() == first_value
                for datum in datumset
            ):
                constant_parts.append(f"{dim_key}: {first_value}")
        if constant_parts:
            return "\n".join(constant_parts)
        return "All data"

    def _format_y_value(self, value, _pos):
        abs_value = abs(value)
        display_value = value
        suffix = ""
        if abs_value >= 1000000:
            display_value = value / 1000000
            suffix = "M"
        elif abs_value >= 1000:
            display_value = value / 1000
            suffix = "K"

        if suffix:
            return f"{display_value:g}{suffix}"
        if value.is_integer():
            return str(int(value))
        return f"{value:g}"

    def _format_y_axis(self, sub_ax):
        sub_ax.yaxis.set_major_formatter(FuncFormatter(self._format_y_value))

    def _get_axes(self, fig, ax):
        n_datumsets = len(self.display_datumsets)
        if n_datumsets == 1:
            axes = [ax]
            return axes, n_datumsets
        fig.clear()
        n_side = math.ceil(math.sqrt(n_datumsets))
        axes = fig.subplots(nrows=n_side, ncols=n_side)
        return axes.flatten(), n_datumsets

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
        self._format_y_axis(sub_ax)
        sub_ax.set_xticks([])
        sub_ax.set_box_aspect(1)
        sub_ax.set_title(
            self._get_subfigure_title(sub_datumset), fontsize=7, pad=3
        )

    def _add_legend(self, fig):
        legend_handles = [
            mpatches.Patch(color=self.x_color_idx[x_value], label=x_value)
            for x_value in self.x_values
        ]
        fig.legend(
            handles=legend_handles,
            title=self.x_dim_key,
            loc="lower center",
            bbox_to_anchor=(0.5, 0.01),
            ncol=min(4, len(legend_handles)),
            frameon=False,
        )

    def _hide_empty_axes(self, axes, n_datumsets):
        for empty_ax in axes[n_datumsets:]:
            empty_ax.set_visible(False)

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_axes(fig, ax)
        y_limit = self._get_y_limit()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(sub_ax, sub_datumset, y_limit)
        self._add_legend(fig)
        self._hide_empty_axes(axes, n_datumsets)
