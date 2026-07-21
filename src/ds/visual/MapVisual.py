import os
import tempfile
import urllib.request

import geopandas

from ds.visual.Visual import Visual

GEO_URL = (
    "https://raw.githubusercontent.com"
    "/nuuuwan/lk_admin_regions/refs/heads/main"
    "/data/geo/topojson/e4_medium"
)
GEO_CACHE_DIR = os.path.join(tempfile.gettempdir(), "datumset_geo")
IMAGE_DIR = "image"


class MapVisual(Visual):

    def __init__(self, datumset, region_dim_key, y_cell_key):
        super().__init__(datumset, region_dim_key, y_cell_key)
        self.region_dim_key = region_dim_key
        self.y_cell_key = y_cell_key

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

    def _image_path(self):
        os.makedirs(IMAGE_DIR, exist_ok=True)
        name = f"map_{self.region_dim_key}_{self.y_cell_key}.png"
        return os.path.join(IMAGE_DIR, name)

    def _load_gdf(self):
        region_type = self.region_dim_key.lower() + "s"
        url = f"{GEO_URL}/{region_type}.topojson"
        os.makedirs(GEO_CACHE_DIR, exist_ok=True)
        cache_path = os.path.join(GEO_CACHE_DIR, f"{region_type}.topojson")
        if not os.path.exists(cache_path):
            urllib.request.urlretrieve(url, cache_path)
        return geopandas.read_file(cache_path)

    def _plot(self, fig, ax):
        region_values = self._get_region_values()
        gdf = self._load_gdf()
        gdf = gdf.rename(columns={"id": "region_id"})
        gdf["value"] = gdf["region_id"].map(region_values)
        gdf.plot(
            column="value",
            ax=ax,
            legend=True,
            cmap="YlOrRd",
            missing_kwds={"color": "#f0f0f0"},
        )
        ax.set_axis_off()
