from utils_future import String

from ds.visual.label_fit.LabelFit import LabelFit


class DorlingLabelMixin:

    LABEL_REF_FONTSIZE = 8

    def _get_circle_char_budget(self, radius, ax, renderer):
        axes_bb = ax.get_window_extent(renderer=renderer)
        xlim = ax.get_xlim()
        span = max(xlim[1] - xlim[0], 1e-9)
        diam_px = axes_bb.width * 2 * radius / span
        sample = ax.text(0, 0, "n" * 10, fontsize=self.LABEL_REF_FONTSIZE)
        char_px = sample.get_window_extent(renderer=renderer).width / 10
        sample.remove()
        return int(diam_px / max(char_px, 1e-9))

    def _add_circle_label(self, ax, renderer, circle, name, color):
        radius = circle[2]
        budget = self._get_circle_char_budget(radius, ax, renderer)
        label = String(name).shorten(max(budget, 1))
        side = radius * 1.4
        fontsize = LabelFit.fit_fontsize(label, side, side, ax, renderer)
        ax.annotate(
            label,
            xy=tuple(circle[1]),
            ha="center",
            va="center",
            fontsize=fontsize,
            color=self._get_contrast_text_color(color),
        )

    def _add_circle_labels(self, fig, ax, circles, gdf):
        renderer = self._get_renderer(fig)
        names = {
            row["region_id"]: row.get("name") or row["region_id"]
            for _, row in gdf.iterrows()
        }
        colors = dict(zip(gdf["region_id"], gdf["color"]))
        for circle in circles:
            region_id = circle[0]
            self._add_circle_label(
                ax,
                renderer,
                circle,
                names.get(region_id, region_id),
                colors.get(region_id, "#cccccc"),
            )
