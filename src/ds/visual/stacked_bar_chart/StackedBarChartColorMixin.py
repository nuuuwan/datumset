class StackedBarChartColorMixin:

    def _get_x_label_colors(self, sub_datumset, x_labels):
        _, stack_labels, data = self._get_data(sub_datumset)
        return [
            self._get_x_label_color(x_label, stack_labels, data)
            for x_label in x_labels
        ]

    def _get_x_label_color(self, x_label, stack_labels, data):
        totals = {s: data[s].get(x_label, 0.0) for s in stack_labels}
        total = sum(totals.values())
        dominant = max(stack_labels, key=lambda s: totals[s])
        pct = totals[dominant] / total if total > 0 else 0.0
        base = self.stack_color_idx[dominant]
        return self._get_share_shaded_color(base, pct)
