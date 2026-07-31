import colorsys

import matplotlib.colors as mcolors


class MapColorMixin:
    MIN_LIGHT, MAX_LIGHT = 0.2, 0.95
    NEUTRAL_COLOR = "#888888"

    def _build_hsl_lightness_cmap(self, base_color):
        h, _, s = colorsys.rgb_to_hls(*mcolors.to_rgb(base_color))
        colors = []
        for i in range(256):
            ratio = i / 255
            new_l = self.MAX_LIGHT + (self.MIN_LIGHT - self.MAX_LIGHT) * ratio
            colors.append(colorsys.hls_to_rgb(h, new_l, s))
        return mcolors.ListedColormap(colors)

    def _get_neutral_cmap(self):
        return self._build_hsl_lightness_cmap(self.NEUTRAL_COLOR)

    def _get_subfigure_base_color(self, sub_datumset):
        datum = sub_datumset[0]
        for dim_key in self._get_dim_labels():
            if dim_key == self.region_dim_key:
                continue
            color_map = self._get_dim_color_map(dim_key)
            if color_map:
                color = color_map.get(datum.dim_idx[dim_key].get_value())
                if color is not None:
                    return color
        return self.NEUTRAL_COLOR

    def _get_subfigure_cmap(self, sub_datumset):
        base_color = self._get_subfigure_base_color(sub_datumset)
        return self._build_hsl_lightness_cmap(base_color)

    def _get_category_color_idx(self):
        categories = self._get_unique_dim_values(self.region_color_dim_key)
        return self._get_dim_color_idx(self.region_color_dim_key, categories)

    def _is_single_map(self):
        return len(self.display_datumsets) == 1

    def _get_single_map_base_color(self):
        return self._get_subfigure_base_color(self.display_datumsets[0])

    def _get_color_context(self):
        if self.region_color_dim_key is not None:
            return {
                "mode": "category",
                "color_idx": self._get_category_color_idx(),
            }
        cmap = self._get_subfigure_cmap(self.display_datumsets[0])
        return {
            "mode": "value",
            "cmap": cmap,
            "values": self._get_sorted_values(),
        }
