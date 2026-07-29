class VisualRectFitMixin:

    def _get_rect_size_px(self, sub_ax, rect):
        x0 = rect.get_x()
        y0 = rect.get_y()
        x1 = x0 + rect.get_width()
        y1 = y0 + rect.get_height()
        px0, py0 = sub_ax.transData.transform((x0, y0))
        px1, py1 = sub_ax.transData.transform((x1, y1))
        return abs(px1 - px0), abs(py1 - py0)

    def _get_rect_fontsize_cap(self, sub_ax, rect):
        max_width_px, max_height_px = self._get_rect_size_px(sub_ax, rect)
        min_dim_px = min(max_width_px, max_height_px)
        px_to_pt = 72.0 / sub_ax.figure.dpi
        return int(min_dim_px * px_to_pt * self.STACK_LABEL_MIN_DIM_RATIO)

    def _get_rect_label_rotation(self, sub_ax, rect):
        width_px, height_px = self._get_rect_size_px(sub_ax, rect)
        return 90 if height_px > width_px else 0

    def _scale_fontsize_to_fit(
        self,
        max_fontsize,
        bbox,
        max_width_px,
        max_height_px,
    ):
        margin = self.STACK_LABEL_BBOX_MARGIN
        w_ratio = (
            max_width_px * margin / bbox.width if bbox.width > 0 else 1.0
        )
        h_ratio = (
            max_height_px * margin / bbox.height if bbox.height > 0 else 1.0
        )
        scale = min(1.0, w_ratio, h_ratio)
        return int(max_fontsize * scale)

    def _get_best_rect_label_fontsize(self, sub_ax, rect, label, rotation):
        renderer = self._get_renderer(sub_ax.figure)
        cx = rect.get_x() + rect.get_width() / 2.0
        cy = rect.get_y() + rect.get_height() / 2.0
        max_width_px, max_height_px = self._get_rect_size_px(sub_ax, rect)
        fontsize_cap = self._get_rect_fontsize_cap(sub_ax, rect)
        if fontsize_cap < self.MIN_STACK_LABEL_FONTSIZE:
            return 0
        max_fontsize = min(self.MAX_STACK_LABEL_FONTSIZE, fontsize_cap)
        probe = sub_ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            rotation=rotation,
            fontsize=max_fontsize,
        )
        bbox = probe.get_window_extent(renderer=renderer)
        probe.remove()
        return self._scale_fontsize_to_fit(
            max_fontsize,
            bbox,
            max_width_px,
            max_height_px,
        )
