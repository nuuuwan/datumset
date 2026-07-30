from collections import defaultdict


class VisualDataMixin:

    def _get_dim_cell_xy(self, datumset, dim_key, cell_key):
        x_labels = []
        y_values = []
        for datum in datumset:
            x_labels.append(datum.dim_idx[dim_key].get_value())
            y_values.append(float(datum.cell_idx[cell_key].get_value()))
        return x_labels, y_values

    def _apply_x_order(self, x_labels, order):
        rank = {x_label: i for i, x_label in enumerate(order)}
        return sorted(x_labels, key=lambda x: rank.get(x, len(order)))

    @staticmethod
    def _dedup_datums(datumset):
        seen = set()
        for datum in datumset:
            key = tuple(
                sorted((k, v.get_value()) for k, v in datum.dim_idx.items())
            )
            if key in seen:
                continue
            seen.add(key)
            yield datum

    def _get_category_cell_xy(self, datumset, dim_key, cell_key):
        totals = {}
        order = []
        for datum in self._dedup_datums(datumset):
            x = self._remap_category(datum.dim_idx[dim_key].get_value())
            v = float(datum.cell_idx[cell_key].get_value())
            if x not in totals:
                totals[x] = 0.0
                order.append(x)
            totals[x] += v
        return order, [totals[x] for x in order]

    def _get_category_value_order(self, dim_key, cell_key):
        order, y_values = self._get_category_cell_xy(
            self.datumset,
            dim_key,
            cell_key,
        )
        if self._is_time_dim(dim_key):
            return sorted(order)
        ordered_values = self._get_ordered_category_valid_values(dim_key)
        if ordered_values is not None:
            return self._apply_x_order(order, ordered_values)
        value_by_x = dict(zip(order, y_values))
        return sorted(order, key=lambda x: value_by_x[x], reverse=True)

    def _get_ordered_category_cell_xy(
        self,
        datumset,
        dim_key,
        cell_key,
        order,
    ):
        x_labels, y_values = self._get_category_cell_xy(
            datumset,
            dim_key,
            cell_key,
        )
        value_by_x = dict(zip(x_labels, y_values))
        sorted_x = self._apply_x_order(x_labels, order)
        return sorted_x, [value_by_x[x] for x in sorted_x]

    def _collect_x_stack_totals(self, x_dim_key, cell_key, stack_dim_key):
        per_x_stack = defaultdict(lambda: defaultdict(float))
        cat_totals = defaultdict(float)
        for datum in self.datumset:
            x = datum.dim_idx[x_dim_key].get_value()
            s = datum.dim_idx[stack_dim_key].get_value()
            v = float(datum.cell_idx[cell_key].get_value())
            per_x_stack[x][s] += v
            cat_totals[s] += v
        return per_x_stack, cat_totals

    def _get_x_dominant_share_order(
        self,
        x_dim_key,
        cell_key,
        stack_dim_key,
    ):
        per_x_stack, cat_totals = self._collect_x_stack_totals(
            x_dim_key,
            cell_key,
            stack_dim_key,
        )
        dominant = max(cat_totals, key=cat_totals.get)

        def share(x):
            total = sum(per_x_stack[x].values())
            return per_x_stack[x][dominant] / total

        return sorted(per_x_stack, key=share, reverse=True)
