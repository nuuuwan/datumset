from collections import defaultdict


class HexMapLabelMixin:

    HEX_LABEL_FONTSIZE = 7

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

    def _add_hex_label(self, ax, region_id, points, names, colors):
        cx = sum(point[0] for point in points) / len(points)
        cy = sum(point[1] for point in points) / len(points)
        ax.annotate(
            names.get(region_id, region_id),
            (cx, cy),
            ha="center",
            va="center",
            fontsize=self.HEX_LABEL_FONTSIZE,
            color=self._get_contrast_text_color(
                colors.get(region_id, "#cccccc")
            ),
        )

    def _add_hex_labels(self, ax, hexes, gdf):
        names = self._get_region_names(gdf)
        colors = self._get_region_colors(gdf)
        for region_id, points in self._get_hex_groups(hexes).items():
            self._add_hex_label(ax, region_id, points, names, colors)
