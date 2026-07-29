from matplotlib.transforms import blended_transform_factory


class VisualUnderlineMixin:

    def _get_x_label_colors(self, sub_datumset, x_labels):
        return None

    def _get_underline_y(self, sub_ax):
        renderer = self._get_renderer(sub_ax.figure)
        labels = sub_ax.get_xticklabels()
        y0_px = min(label.get_window_extent(renderer).y0 for label in labels)
        y_frac = sub_ax.transAxes.inverted().transform((0, y0_px))[1]
        return y_frac - self.X_LABEL_UNDERLINE_GAP

    def _underline_x_labels(self, sub_ax, positions, colors, half_widths):
        y = self._get_underline_y(sub_ax)
        trans = blended_transform_factory(
            sub_ax.transData,
            sub_ax.transAxes,
        )
        for x, color, half in zip(positions, colors, half_widths):
            sub_ax.plot(
                [x - half, x + half],
                [y, y],
                transform=trans,
                color=color,
                linewidth=self.X_LABEL_UNDERLINE_LW,
                solid_capstyle="round",
                clip_on=False,
                zorder=5,
            )
