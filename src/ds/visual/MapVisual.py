import os
import tempfile
import urllib.request

import geopandas
import matplotlib.cm as cm
import matplotlib.colors as mcolors

from ds.visual.label_fit.LabelFit import LabelFit
from ds.visual.Visual import Visual

GEO_URL = (
    "https://raw.githubusercontent.com"
    "/nuuuwan/lk_admin_regions/refs/heads/main"
    "/data/geo/topojson/e4_medium"
)
GEO_CACHE_DIR = os.path.join(tempfile.gettempdir(), "datumset_geo")
IMAGE_DIR = "image"


class MapVisual(Visual):

    def __init__(
        self,
        datumset,
        region_dim_key=None,
        y_cell_key=None,
    ):
        super().__init__(datumset)
        query = datumset[0].query
        self.region_dim_key = region_dim_key or query.dim_labels[1]
        self.y_cell_key = y_cell_key or query.cell_labels[0]
        self.display_datumsets = self._get_display_datumsets(
            {self.region_dim_key}
        )

    def _get_region_values(self):
        return {
            datum.dim_idx[self.region_dim_key].get_value(): float(
                datum.cell_idx[self.y_cell_key].get_value()
            )
            for datum in self.datumset
        }

    def _excluded_dim_keys(self):
        return {self.region_dim_key}

    def _build_title(self):
        return f"{self.y_cell_key} by {self.region_dim_key}"

    def _get_title_text(self):
        entity = self.datumset[0].entity_class.__name__
        return f"{entity} {self.y_cell_key} by {self.region_dim_key}"

    def _load_gdf(self):
        region_type = self.region_dim_key.lower() + "s"
        url = f"{GEO_URL}/{region_type}.topojson"
        os.makedirs(GEO_CACHE_DIR, exist_ok=True)
        cache_path = os.path.join(GEO_CACHE_DIR, f"{region_type}.topojson")
        if not os.path.exists(cache_path):
            urllib.request.urlretrieve(url, cache_path)
        return geopandas.read_file(cache_path)

    def _add_region_labels(self, gdf, ax, fig):
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        for _, row in gdf.iterrows():
            label = row.get("name") or row["region_id"]
            cx, cy, rw, rh, angle_deg = LabelFit.best_label_fit(row.geometry)
            fontsize = LabelFit.fit_fontsize(label, rw, rh, ax, renderer)
            text_angle = angle_deg if rw >= rh else angle_deg + 90
            while text_angle > 90:
                text_angle -= 180
            ax.annotate(
                label,
                xy=(cx, cy),
                ha="center",
                va="center",
                fontsize=fontsize,
                color="#333333",
                rotation=text_angle,
            )

    def _get_value_range(self):
        min_value = None
        max_value = None
        for sub_datumset in self.display_datumsets:
            values = self._get_region_values_for(sub_datumset).values()
            for value in values:
                min_value = (
                    value if min_value is None else min(min_value, value)
                )
                max_value = (
                    value if max_value is None else max(max_value, value)
                )
        if min_value is None or max_value is None:
            return 0.0, 1.0
        if min_value == max_value:
            return min_value, min_value + 1.0
        return min_value, max_value

    def _get_region_values_for(self, datumset):
        return {
            datum.dim_idx[self.region_dim_key].get_value(): float(
                datum.cell_idx[self.y_cell_key].get_value()
            )
            for datum in datumset
        }

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, vmin, vmax):
        region_values = self._get_region_values_for(sub_datumset)
        gdf = self._load_gdf().rename(columns={"id": "region_id"})
        gdf["value"] = gdf["region_id"].map(region_values)
        gdf.plot(
            column="value",
            ax=sub_ax,
            legend=False,
            cmap="YlOrRd",
            vmin=vmin,
            vmax=vmax,
            missing_kwds={"color": "#f0f0f0"},
        )
        self._add_region_labels(gdf, sub_ax, fig)
        sub_ax.set_axis_off()
        sub_ax.set_box_aspect(1)
        sub_ax.set_title(
            self._get_subfigure_title(sub_datumset, {self.region_dim_key}),
            fontsize=7,
            pad=3,
        )

    def _add_colorbar(self, fig, vmin, vmax):
        scalar_mappable = cm.ScalarMappable(
            norm=mcolors.Normalize(vmin=vmin, vmax=vmax),
            cmap="YlOrRd",
        )
        scalar_mappable.set_array([])
        colorbar = fig.colorbar(
            scalar_mappable,
            ax=fig.axes,
            orientation="horizontal",
            fraction=0.04,
            pad=0.04,
        )
        colorbar.set_label(self.y_cell_key)

    def _plot(self, fig, ax):
        n_datumsets = len(self.display_datumsets)
        axes = self._get_square_axes(fig, ax, n_datumsets)
        vmin, vmax = self._get_value_range()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(fig, sub_ax, sub_datumset, vmin, vmax)
        self._add_colorbar(fig, vmin, vmax)
        self._hide_empty_axes(axes, n_datumsets)
