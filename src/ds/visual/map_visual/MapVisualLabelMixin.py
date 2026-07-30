from utils_future import String

from ds.visual.label_fit.LabelFit import LabelFit


class MapVisualLabelMixin:

    LABEL_MIN_FONTSIZE = 8

    def _fit_label_text(self, label, rw, rh, ax, renderer):
        full_size = LabelFit.fit_fontsize(label, rw, rh, ax, renderer)
        if full_size >= self.LABEL_MIN_FONTSIZE:
            return label
        short = String(label).shorten(3)
        short_size = LabelFit.fit_fontsize(short, rw, rh, ax, renderer)
        return short if short_size > full_size else label

    def _get_label_angle(self, angle_deg, rw, rh):
        text_angle = angle_deg if rw >= rh else angle_deg + 90
        while text_angle > 90:
            text_angle -= 180
        return text_angle

    def _add_region_label(self, ax, renderer, row):
        label = row.get("name") or row["region_id"]
        cx, cy, rw, rh, angle_deg = LabelFit.best_label_fit(row.geometry)
        label = self._fit_label_text(label, rw, rh, ax, renderer)
        fontsize = LabelFit.fit_fontsize(label, rw, rh, ax, renderer)
        fontsize = max(4, min(9, fontsize))
        ax.annotate(
            label,
            xy=(cx, cy),
            ha="center",
            va="center",
            fontsize=fontsize,
            color=self._get_contrast_text_color(row["color"]),
            rotation=self._get_label_angle(angle_deg, rw, rh),
            clip_on=True,
        )

    def _add_region_labels(self, gdf, ax, fig):
        renderer = self._get_renderer(fig)
        for _, row in gdf.iterrows():
            self._add_region_label(ax, renderer, row)
