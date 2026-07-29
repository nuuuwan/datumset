import colorsys

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


class VisualColorMixin:

    OTHER_CATEGORY_COLOR = "#999999"

    def _get_default_color_idx(self, dim_values):
        cmap = plt.get_cmap("tab20")
        return {
            dim_value: cmap(i % cmap.N)
            for i, dim_value in enumerate(dim_values)
        }

    def _get_dim_color_map(self, dim_key):
        concept = self.datumset[0].dim_idx.get(dim_key)
        color_map = None
        if concept is not None:
            concept_class = concept.__class__
            get_color_map = getattr(concept_class, "get_color_map", None)
            if get_color_map is not None:
                maybe_color_map = get_color_map()
                if isinstance(maybe_color_map, dict):
                    color_map = maybe_color_map
        return color_map

    def _get_category_color(self, dim_value, color_map, default_color_idx):
        if dim_value == self.OTHER_CATEGORY:
            return self.OTHER_CATEGORY_COLOR
        if color_map:
            return color_map.get(dim_value, default_color_idx[dim_value])
        return default_color_idx[dim_value]

    def _get_dim_color_idx(self, dim_key, dim_values):
        default_color_idx = self._get_default_color_idx(dim_values)
        color_map = self._get_dim_color_map(dim_key)
        return {
            dim_value: self._get_category_color(
                dim_value,
                color_map,
                default_color_idx,
            )
            for dim_value in dim_values
        }

    def _get_fixed_dim_color(self, dim_key):
        dim_values = self._get_unique_dim_values(dim_key)
        if len(dim_values) != 1:
            return None
        color_map = self._get_dim_color_map(dim_key)
        if not color_map:
            return None
        dim_value = dim_values[0]
        return color_map.get(dim_value)

    def _get_single_fixed_dim_color(self, excluded_dim_keys=None):
        excluded_dim_keys = excluded_dim_keys or set()
        for dim_key in self._get_dim_labels():
            if dim_key in excluded_dim_keys:
                continue
            color = self._get_fixed_dim_color(dim_key)
            if color is not None:
                return color
        return None

    def _get_share_shaded_color(self, base_color, pct):
        h, s, v = colorsys.rgb_to_hsv(*mcolors.to_rgb(base_color))
        pct = max(0.0, min(1.0, pct))
        s2 = s * pct
        v2 = v + (1.0 - v) * (1.0 - pct)
        return colorsys.hsv_to_rgb(h, s2, v2)
