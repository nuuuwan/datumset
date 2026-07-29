import colorsys

import matplotlib.colors as mcolors


class MapVisualColorMixin:

    def _get_region_label_color(self, value, vmin, vmax, cmap):
        color = cmap((value - vmin) / (vmax - vmin))
        return self._get_contrast_text_color(color)

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
