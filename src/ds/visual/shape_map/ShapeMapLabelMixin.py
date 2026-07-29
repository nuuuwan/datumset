from collections import defaultdict

from utils_future import String

from ds.visual.label_fit.LabelFit import LabelFit


class ShapeMapLabelMixin:

    LABEL_REF_FONTSIZE = 8

    def _get_char_budget(self, rect_w, ax, renderer):
        axes_bb = ax.get_window_extent(renderer=renderer)
        xlim = ax.get_xlim()
        span = max(xlim[1] - xlim[0], 1e-9)
        rect_px = axes_bb.width * rect_w / span
        sample = ax.text(0, 0, "n" * 10, fontsize=self.LABEL_REF_FONTSIZE)
        char_px = sample.get_window_extent(renderer=renderer).width / 10
        sample.remove()
        return int(rect_px / max(char_px, 1e-9))

    def _shorten_to_fit(self, label, rect_w, ax, renderer):
        budget = self._get_char_budget(rect_w, ax, renderer)
        return String(label).shorten(max(budget, 1))

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
        label = self._shorten_to_fit(label, rect_w, ax, renderer)
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
