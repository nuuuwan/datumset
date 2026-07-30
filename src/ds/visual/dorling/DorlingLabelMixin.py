from utils_future import String

from ds.visual.label_fit.LabelFit import LabelFit


class DorlingLabelMixin:

    LABEL_FONTSIZE = 11

    def _add_circle_label(self, ax, renderer, circle, name, color):
        radius = circle[2]
        diam = radius * 2
        budget = LabelFit.char_budget(
            diam, diam, self.LABEL_FONTSIZE, ax, renderer
        )
        label = String(name).shorten(max(budget, 1))
        ax.annotate(
            label,
            xy=tuple(circle[1]),
            ha="center",
            va="center",
            fontsize=self.LABEL_FONTSIZE,
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
