from utils_future import Percent


class VisualRectLabelMixin:

    STACK_LABEL_FONT_REDUCTION = 1

    def _add_bar_totals(self, sub_ax, x_values, totals, y_limit):
        offset = y_limit * 0.015
        for x_value, total in zip(x_values, totals):
            sub_ax.text(
                x_value,
                total + offset,
                self._format_y_value(total),
                ha="center",
                va="bottom",
                fontsize=7,
                color=self.SUBTITLE_COLOR,
            )

    def _add_fitted_label_in_rect(self, sub_ax, rect, label):
        rotation = self._get_rect_label_rotation(sub_ax, rect)
        fontsize = self._get_best_rect_label_fontsize(
            sub_ax,
            rect,
            label,
            rotation,
        )
        fontsize -= self.STACK_LABEL_FONT_REDUCTION
        if fontsize < self.MIN_STACK_LABEL_FONTSIZE:
            return
        cx = rect.get_x() + rect.get_width() / 2.0
        cy = rect.get_y() + rect.get_height() / 2.0
        sub_ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            rotation=rotation,
            fontsize=fontsize,
            color=self._get_contrast_text_color(rect.get_facecolor()),
        )

    def _add_stacked_bar_percentages(self, sub_ax, bars, values, totals):
        for i, rect in enumerate(bars):
            value = values[i]
            total = totals[i]
            if value <= 0 or total <= 0:
                continue
            label = Percent(value / total).humanize
            self._add_fitted_label_in_rect(sub_ax, rect, label)
