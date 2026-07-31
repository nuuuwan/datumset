class TreeMapLabelMixin:

    LABEL_FONT_REDUCTION = 1

    def _add_rect_label(self, sub_ax, rect, x_label, value, total):
        width = rect.get_width()
        height = rect.get_height()
        area_ratio = width * height
        if area_ratio < self.MIN_LABEL_AREA_RATIO:
            return
        label = self._format_tree_map_label(x_label, value)
        fontsize = self._get_best_rect_label_fontsize(
            sub_ax,
            rect,
            label,
            self._get_rect_label_rotation(sub_ax, rect),
        )
        fontsize -= self.LABEL_FONT_REDUCTION
        if fontsize < self.MIN_STACK_LABEL_FONTSIZE:
            return
        cx = rect.get_x() + width / 2.0
        cy = rect.get_y() + height / 2.0
        sub_ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            fontsize=fontsize,
            color=self._get_contrast_text_color(rect.get_facecolor()),
        )

    def _format_tree_map_label(self, x_label, value):
        value_text = self._format_y_value(value)
        display_label = self._format_visual_value(x_label)
        return f"{display_label}\n({value_text})"
