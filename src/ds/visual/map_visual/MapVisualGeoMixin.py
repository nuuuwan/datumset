import os
import tempfile
import urllib.request
from collections import defaultdict

import geopandas
from utils_future import String

GEO_URL = (
    "https://raw.githubusercontent.com"
    "/nuuuwan/lk_admin_regions/refs/heads/main"
    "/data/geo/topojson/e4_medium"
)
GEO_CACHE_DIR = os.path.join(tempfile.gettempdir(), "datumset_geo")


class MapVisualGeoMixin:

    def _normalize_region_key(self, raw_value):
        return String(raw_value).snake

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

    def _get_region_winner_category(self, sub_datumset):
        totals = defaultdict(lambda: defaultdict(float))
        for datum in sub_datumset:
            region = self._normalize_region_key(
                datum.dim_idx[self.region_dim_key].get_value()
            )
            category = datum.dim_idx[self.region_color_dim_key].get_value()
            value = float(datum.cell_idx[self.y_cell_key].get_value())
            totals[region][category] += value
        return {
            region: max(cats, key=cats.get) for region, cats in totals.items()
        }

    def _lookup_region_category(self, row, winners):
        for raw_key in (row.get("region_id"), row.get("name")):
            normalized_key = self._normalize_region_key(raw_key)
            if normalized_key in winners:
                return winners[normalized_key]
        return None

    def _get_category_region_counts(self):
        counts = defaultdict(int)
        for sub_datumset in self.display_datumsets:
            winners = self._get_region_winner_category(sub_datumset)
            for category in winners.values():
                counts[category] += 1
        return counts

    def _get_sorted_values(self):
        values = set()
        for sub_datumset in self.display_datumsets:
            values.update(self._get_region_percentages(sub_datumset).values())
        return sorted(values)
