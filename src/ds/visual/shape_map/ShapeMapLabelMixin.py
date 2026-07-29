from collections import defaultdict

from ds.visual.label_fit.LabelFit import LabelFit


class ShapeMapLabelMixin:

    def _get_region_names(self, gdf):
        return {
            row["region_id"]: row.get("name") or row["region_id"]
            for _, row in gdf.iterrows()
        }

    def _get_region_colors(self, gdf):
        return dict(zip(gdf["region_id"], gdf["color"]))

    @staticmethod
    def _get_shape_groups(shapes):
        groups = defaultdict(list)
        for region_id, x, y in shapes:
            groups[region_id].append((x, y))
        return groups

    def _add_shape_label(self, ax, renderer, radius, label, points, color):
        cx, cy, rect_w, rect_h, angle = self._best_label_fit(points, radius)
        label = self._fit_label_text(label, rect_w, rect_h, ax, renderer)
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

    def _add_shape_labels(self, fig, ax, radius, shapes, gdf):
        renderer = self._get_renderer(fig)
        names = self._get_region_names(gdf)
        colors = self._get_region_colors(gdf)
        for region_id, points in self._get_shape_groups(shapes).items():
            self._add_shape_label(
                ax,
                renderer,
                radius,
                names.get(region_id, region_id),
                points,
                colors.get(region_id, "#cccccc"),
            )
