import colorsys
import os
import tempfile
import urllib.request

import geopandas
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.ticker import FuncFormatter

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
        self.region_dim_key = self._resolve_dim_key(region_dim_key, 1)
        self.y_cell_key = self._resolve_cell_key(y_cell_key)
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
        return self._build_dim_title(self.y_cell_key, self.region_dim_key)

    def _get_title_text(self):
        return self._build_entity_dim_title(
            self.y_cell_key,
            self.region_dim_key,
        )

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
            if rw <= 0 or rh <= 0:
                continue
            fontsize = LabelFit.fit_fontsize(label, rw, rh, ax, renderer)
            fontsize = max(4, min(9, fontsize))
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
                clip_on=True,
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

    def _build_hsl_lightness_cmap(self, base_color):
        base_rgb = mcolors.to_rgb(base_color)
        h, l, s = colorsys.rgb_to_hls(*base_rgb)
        light_l = min(0.95, max(0.55, l * 1.2))
        dark_l = max(0.12, min(0.45, l * 0.6))
        if dark_l >= light_l:
            dark_l = max(0.0, light_l - 0.25)
        colors = []
        for i in range(256):
            ratio = i / 255
            new_l = light_l + (dark_l - light_l) * ratio
            colors.append(colorsys.hls_to_rgb(h, new_l, s))
        return mcolors.ListedColormap(colors)

    def _get_value_cmap(self):
        base_color = self._get_single_fixed_dim_color({self.region_dim_key})
        if base_color is None:
            return "YlOrRd"
        return self._build_hsl_lightness_cmap(base_color)

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, vmin, vmax, cmap):
        region_values = self._get_region_values_for(sub_datumset)
        gdf = self._load_gdf().rename(columns={"id": "region_id"})
        gdf["value"] = gdf["region_id"].map(region_values)
        gdf.plot(
            column="value",
            ax=sub_ax,
            legend=False,
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            missing_kwds={"color": "#f0f0f0"},
        )
        self._add_region_labels(gdf, sub_ax, fig)
        sub_ax.set_axis_off()
        self._set_square_subfigure_title(sub_ax, sub_datumset)

    def _add_colorbar(self, fig, vmin, vmax, cmap):
        scalar_mappable = cm.ScalarMappable(
            norm=mcolors.Normalize(vmin=vmin, vmax=vmax),
            cmap=cmap,
        )
        scalar_mappable.set_array([])
        colorbar = fig.colorbar(
            scalar_mappable,
            ax=fig.axes,
            orientation="horizontal",
            fraction=0.04,
            pad=0.04,
        )
        formatter = FuncFormatter(self._format_humanized_value)
        colorbar.formatter = formatter
        colorbar.ax.xaxis.set_major_formatter(formatter)
        colorbar.ax.xaxis.offsetText.set_visible(False)
        colorbar.update_ticks()
        colorbar.set_label(self.y_cell_key)

    def _plot(self, fig, ax):
        axes, n_datumsets = self._get_display_axes(
            fig,
            ax,
            self.display_datumsets,
        )
        vmin, vmax = self._get_value_range()
        cmap = self._get_value_cmap()
        for sub_ax, sub_datumset in zip(axes, self.display_datumsets):
            self._plot_subfigure(
                fig,
                sub_ax,
                sub_datumset,
                vmin,
                vmax,
                cmap,
            )
        self._add_colorbar(fig, vmin, vmax, cmap)
        self._hide_empty_axes(axes, n_datumsets)
