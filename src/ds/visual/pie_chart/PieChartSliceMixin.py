import math


class PieChartSliceMixin:

    def _build_autopct(self):
        def _autopct(pct):
            if pct > 0.5:
                return f"{pct:.0f}%"
            return "<0.5%"

        return _autopct

    def _get_total_value_text(self, y_values):
        total = sum(y_values)
        return self._format_humanized_value(total, None)

    def _get_pie_radius(self, total, max_total, n_datumsets):
        if n_datumsets <= 1 or max_total <= 0:
            return 1.0
        scale = math.sqrt(total / max_total) if total > 0 else 0.0
        return max(0.3, scale)

    def _set_subfigure_title_with_total(self, sub_ax, sub_datumset, y_values):
        total_text = self._get_total_value_text(y_values)
        if len(self.display_datumsets) <= 1:
            title = total_text
        else:
            base_title = self._get_subfigure_title_text(
                sub_datumset,
                self._excluded_dim_keys(),
            )
            title = f"{base_title}\n{total_text}"
        sub_ax.set_title(
            title,
            fontsize=self.SUBFIGURE_TITLE_FONTSIZE,
            pad=self.SUBFIGURE_TITLE_PAD,
        )

    def _get_sub_datumset_total(self, sub_datumset):
        _, y_values = self._get_dim_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
        )
        return sum(y_values)

    def _get_sorted_slice_data(self, x_labels, y_values):
        combined = sorted(
            zip(x_labels, y_values),
            key=lambda item: item[1],
            reverse=True,
        )
        if not combined:
            return [], []
        sorted_x_labels, sorted_y_values = zip(*combined)
        return list(sorted_x_labels), list(sorted_y_values)
