import colorsys

import matplotlib.colors as mcolors


class MapVisualColorMixin:

    def _build_hsl_lightness_cmap(self, base_color):
        base_rgb = mcolors.to_rgb(base_color)
        h, l, s = colorsys.rgb_to_hls(*base_rgb)
        light_l = min(0.95, max(0.55, l * 1.2))
        dark_l = max(0.12, min(0.45, l * 0.6))
        colors = []
        for i in range(256):
            ratio = i / 255
            new_l = light_l + (dark_l - light_l) * ratio
            colors.append(colorsys.hls_to_rgb(h, new_l, s))
        return mcolors.ListedColormap(colors)

    def _get_value_cmap(self):
        base_color = self._get_single_fixed_dim_color({self.region_dim_key})
        return self._build_hsl_lightness_cmap(base_color)

    def _get_category_color_idx(self):
        categories = self._get_unique_dim_values(self.region_color_dim_key)
        return self._get_dim_color_idx(self.region_color_dim_key, categories)

    def _get_color_context(self):
        if self.region_color_dim_key is not None:
            return {
                "mode": "category",
                "color_idx": self._get_category_color_idx(),
            }
        vmin, vmax = self._get_value_range()
        return {
            "mode": "value",
            "vmin": vmin,
            "vmax": vmax,
            "cmap": self._get_value_cmap(),
        }
