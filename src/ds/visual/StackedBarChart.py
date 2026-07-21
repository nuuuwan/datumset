import os
from collections import defaultdict

from ds.visual.Visual import Visual

IMAGE_DIR = "image"


class StackedBarChart(Visual):

    def __init__(self, datumset, x_dim_key, stack_dim_key, y_cell_key):
        super().__init__(datumset, x_dim_key, stack_dim_key, y_cell_key)
        self.x_dim_key = x_dim_key
        self.stack_dim_key = stack_dim_key
        self.y_cell_key = y_cell_key

    def _get_data(self):
        x_labels, stack_labels = [], []
        data = defaultdict(dict)
        for datum in self.datumset:
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

    def _image_path(self):
        os.makedirs(IMAGE_DIR, exist_ok=True)
        name = (
            f"stacked_barchart"
            f"_{self.x_dim_key}_{self.stack_dim_key}_{self.y_cell_key}.png"
        )
        return os.path.join(IMAGE_DIR, name)

    def _plot(self, fig, ax):
        x_labels, stack_labels, data = self._get_data()
        bottoms = [0.0] * len(x_labels)
        for s in stack_labels:
            values = [data[s].get(x, 0.0) for x in x_labels]
            ax.bar(x_labels, values, bottom=bottoms, label=s)
            bottoms = [b + v for b, v in zip(bottoms, values)]
        ax.set_xlabel(self.x_dim_key)
        ax.set_ylabel(self.y_cell_key)
        ax.legend(title=self.stack_dim_key)
        ax.set_xticks(range(len(x_labels)))
        ax.set_xticklabels(x_labels, rotation=45, ha="right")
