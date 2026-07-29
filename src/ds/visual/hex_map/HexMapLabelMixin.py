from collections import defaultdict

from ds.visual.hex_map.HexTextFit import HexTextFit
from ds.visual.label_fit.LabelFit import LabelFit


class HexMapLabelMixin:

    def _get_region_names(self, gdf):
        return {
            row["region_id"]: row.get("name") or row["region_id"]
            for _, row in gdf.iterrows()
        }

    def _get_region_colors(self, gdf):
        return dict(zip(gdf["region_id"], gdf["color"]))

    @staticmethod
    def _get_hex_groups(hexes):
        groups = defaultdict(list)
        for region_id, x, y in hexes:
            groups[region_id].append((x, y))
        return groups

    def _add_hex_label(self, ax, renderer, radius, label, points, color):
        cx, cy, rect_w, rect_h, angle = HexTextFit.best_label_fit(
            points, radius
        )
        fontsize = LabelFit.fit_fontsize(label, rect_w, rect_h, ax, renderer)
        ax.annotate(
            label,
            xy=(cx, cy),
            ha="center",
            va="center",
            fontsize=fontsize,
            rotation=angle,
            color=self._get_contrast_text_color(color),
        )

    def _add_hex_labels(self, fig, ax, radius, hexes, gdf):
        renderer = self._get_renderer(fig)
        names = self._get_region_names(gdf)
        colors = self._get_region_colors(gdf)
        for region_id, points in self._get_hex_groups(hexes).items():
            self._add_hex_label(
                ax,
                renderer,
                radius,
                names.get(region_id, region_id),
                points,
                colors.get(region_id, "#cccccc"),
            )
