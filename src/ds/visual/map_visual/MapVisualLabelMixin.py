from ds.visual.label_fit.LabelFit import LabelFit


class MapVisualLabelMixin:

    def _add_region_labels(self, gdf, ax, fig, vmin, vmax, cmap):
        renderer = self._get_renderer(fig)
        for _, row in gdf.iterrows():
            label = row.get("name") or row["region_id"]
            cx, cy, rw, rh, angle_deg = LabelFit.best_label_fit(row.geometry)
            if rw <= 0 or rh <= 0:
                continue
            fontsize = LabelFit.fit_fontsize(label, rw, rh, ax, renderer)
            fontsize = max(4, min(9, fontsize))
            text_angle = angle_deg if rw >= rh else angle_deg + 90
            while text_angle > 90:
                text_angle -= 180
            text_color = self._get_region_label_color(
                row.get("value"),
                vmin,
                vmax,
                cmap,
            )
            ax.annotate(
                label,
                xy=(cx, cy),
                ha="center",
                va="center",
                fontsize=fontsize,
                color=text_color,
                rotation=text_angle,
                clip_on=True,
            )
