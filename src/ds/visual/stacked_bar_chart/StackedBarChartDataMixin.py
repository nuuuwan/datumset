from collections import defaultdict


class StackedBarChartDataMixin:

    def _get_data(self, datumset):
        x_labels, stack_labels = [], []
        data = defaultdict(dict)
        for datum in datumset:
            x = datum.dim_idx[self.x_dim_key].get_value()
            s = self._remap_category(
                datum.dim_idx[self.stack_dim_key].get_value()
            )
            v = float(datum.cell_idx[self.y_cell_key].get_value())
            if x not in x_labels:
                x_labels.append(x)
            if s not in stack_labels:
                stack_labels.append(s)
            data[s][x] = data[s].get(x, 0.0) + v
        x_labels = self._apply_x_order(x_labels, self._get_x_order())
        return x_labels, stack_labels, data

    def _get_x_order(self):
        ordered_values = self._get_ordered_category_valid_values(
            self.x_dim_key
        )
        if ordered_values is not None:
            return ordered_values
        return self._get_x_total_value_order(
            self.x_dim_key,
            self.y_cell_key,
            self.stack_dim_key,
        )

    def _get_sorted_stack_labels_for_x(self, stack_labels, data, x_label):
        return sorted(
            stack_labels,
            key=lambda stack_label: data[stack_label].get(x_label, 0.0),
            reverse=False,
        )

    def _get_totals(self, x_labels, data):
        totals = []
        for x_label in x_labels:
            total = sum(
                stack_data.get(x_label, 0.0) for stack_data in data.values()
            )
            totals.append(total)
        return totals

    def _get_column_key(self, datum):
        return tuple(
            (k, c.get_value())
            for k, c in datum.dim_idx.items()
            if k != self.stack_dim_key
        )

    def _get_category_win_counts(self):
        groups = defaultdict(lambda: defaultdict(float))
        for datum in self.datumset:
            key = self._get_column_key(datum)
            s = self._remap_category(
                datum.dim_idx[self.stack_dim_key].get_value()
            )
            v = float(datum.cell_idx[self.y_cell_key].get_value())
            groups[key][s] += v
        counts = defaultdict(int)
        for stacks in groups.values():
            counts[max(stacks, key=stacks.get)] += 1
        return counts
