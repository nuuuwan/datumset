from ds.visual.Visual import Visual

IMAGE_DIR = "image"


class BarChart(Visual):

    def __init__(
        self,
        datumset,
        x_dim_key=None,
        y_cell_key=None,
    ):
        super().__init__(datumset)
        query = datumset[0].query
        self.x_dim_key = x_dim_key or query.dim_labels[0]
        self.y_cell_key = y_cell_key or query.cell_labels[0]

    def _get_xy(self):
        x_labels = []
        y_values = []
        for datum in self.datumset:
            x_labels.append(datum.dim_idx[self.x_dim_key].get_value())
            y_values.append(
                float(datum.cell_idx[self.y_cell_key].get_value())
            )
        return x_labels, y_values

    def _excluded_dim_keys(self):
        return {self.x_dim_key}

    def _build_title(self):
        return f"{self.y_cell_key} by {self.x_dim_key}"

    def _plot(self, fig, ax):
        x_labels, y_values = self._get_xy()
        ax.bar(x_labels, y_values)
        ax.set_xlabel(self.x_dim_key)
        ax.set_ylabel(self.y_cell_key)
        ax.set_xticks(range(len(x_labels)))
        ax.set_xticklabels(x_labels, rotation=45, ha="right")
