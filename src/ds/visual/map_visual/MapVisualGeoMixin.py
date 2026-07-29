import os
import tempfile
import urllib.request

import geopandas

GEO_URL = (
    "https://raw.githubusercontent.com"
    "/nuuuwan/lk_admin_regions/refs/heads/main"
    "/data/geo/topojson/e4_medium"
)
GEO_CACHE_DIR = os.path.join(tempfile.gettempdir(), "datumset_geo")


class MapVisualGeoMixin:

    def _normalize_region_key(self, raw_value):
        return (
            str(raw_value).strip().lower().replace("-", "_").replace(" ", "_")
        )

    def _load_gdf(self):
        region_type = self.region_dim_key.lower() + "s"
        url = f"{GEO_URL}/{region_type}.topojson"
        os.makedirs(GEO_CACHE_DIR, exist_ok=True)
        cache_path = os.path.join(GEO_CACHE_DIR, f"{region_type}.topojson")
        if not os.path.exists(cache_path):
            urllib.request.urlretrieve(url, cache_path)  # pragma: no cover
        return geopandas.read_file(cache_path)

    def _get_region_values_for(self, datumset):
        return {
            self._normalize_region_key(
                datum.dim_idx[self.region_dim_key].get_value()
            ): float(datum.cell_idx[self.y_cell_key].get_value())
            for datum in datumset
        }

    def _lookup_region_value(self, row, region_values):
        for raw_key in (row.get("region_id"), row.get("name")):
            normalized_key = self._normalize_region_key(raw_key)
            if normalized_key in region_values:
                return region_values[normalized_key]
        return None

    def _get_gdf_with_values(self, sub_datumset):
        region_values = self._get_region_values_for(sub_datumset)
        gdf = self._load_gdf().rename(columns={"id": "region_id"})
        gdf["value"] = gdf.apply(
            lambda row: self._lookup_region_value(row, region_values),
            axis=1,
        )
        return gdf[gdf["value"].notna()].copy()

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
        return min_value, max_value
