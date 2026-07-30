from utils_future import String

from ds.visual.label_fit.LabelFit import LabelFit


class MapVisualLabelMixin:

    LABEL_FONTSIZE = 10

    def _get_label_angle(self, angle_deg, rw, rh):
        text_angle = angle_deg if rw >= rh else angle_deg + 90
        while text_angle > 90:
            text_angle -= 180
        return text_angle

    def _add_region_label(self, ax, renderer, row):
        label = row.get("name") or row["region_id"]
        cx, cy, rw, rh, angle_deg = LabelFit.best_label_fit(row.geometry)
        budget = LabelFit.char_budget(
            rw, rh, self.LABEL_FONTSIZE, ax, renderer
        )
        label = String(label).shorten(max(budget, 1))
        ax.annotate(
            label,
            xy=(cx, cy),
            ha="center",
            va="center",
            fontsize=self.LABEL_FONTSIZE,
            color=self._get_contrast_text_color(row["color"]),
            rotation=self._get_label_angle(angle_deg, rw, rh),
            clip_on=True,
        )

    def _add_region_labels(self, gdf, ax, fig):
        renderer = self._get_renderer(fig)
        for _, row in gdf.iterrows():
            self._add_region_label(ax, renderer, row)
