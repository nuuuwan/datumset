import os

from ds.visual.Visual import Visual

IMAGE_DIR = "image"


class BarChart(Visual):

    def __init__(self, datumset, x_dim_key, y_cell_key):
        super().__init__(datumset, x_dim_key, y_cell_key)
        self.x_dim_key = x_dim_key
        self.y_cell_key = y_cell_key

    def _get_xy(self):
        x_labels = []
        y_values = []
        for datum in self.datumset:
            x_labels.append(datum.dim_idx[self.x_dim_key].get_value())
            y_values.append(float(datum.cell_idx[self.y_cell_key].get_value()))
        return x_labels, y_values

    def _excluded_dim_keys(self):
        return {self.x_dim_key}

    def _build_title(self):
        return f"{self.y_cell_key} by {self.x_dim_key}"

    def _image_path(self):
        os.makedirs(IMAGE_DIR, exist_ok=True)
        name = f"barchart_{self.x_dim_key}_{self.y_cell_key}.png"
        return os.path.join(IMAGE_DIR, name)

    def _plot(self, fig, ax):
        x_labels, y_values = self._get_xy()
        ax.bar(x_labels, y_values)
        ax.set_xlabel(self.x_dim_key)
        ax.set_ylabel(self.y_cell_key)
        ax.set_xticks(range(len(x_labels)))
        ax.set_xticklabels(x_labels, rotation=45, ha="right")
