class TreeMapDataMixin:

    def _get_tree_map_data(self, sub_datumset):
        x_labels, y_values = self._get_category_cell_xy(
            sub_datumset,
            self.x_dim_key,
            self.y_cell_key,
        )
        order = self._get_value_order(x_labels, y_values)
        x_labels, y_values = self._sort_by_order(
            x_labels,
            y_values,
            order,
        )
        total = sum(y_values) or 1.0
        return x_labels, y_values, total

    def _get_value_order(self, x_labels, y_values):
        ordered_values = self._get_ordered_category_valid_values(
            self.x_dim_key
        )
        if ordered_values is not None:
            return ordered_values
        value_by_x = dict(zip(x_labels, y_values))
        return sorted(x_labels, key=lambda x: value_by_x[x], reverse=True)

    @staticmethod
    def _sort_by_order(x_labels, y_values, order):
        rank = {x_label: i for i, x_label in enumerate(order)}
        combined = sorted(
            zip(x_labels, y_values),
            key=lambda item: rank.get(item[0], len(order)),
        )
        return [item[0] for item in combined], [item[1] for item in combined]

    def _append_to_rows(self, rows, current, n_rows):
        if not current:
            return rows
        if len(rows) < n_rows:
            rows.append(current)
        else:
            rows[-1].extend(current)
        return rows

    def _split_rows(self, values, n_rows):
        target_total = sum(values) / n_rows if n_rows > 0 else 0.0
        rows = []
        current = [values[0]]
        current_total = values[0]
        for value in values[1:]:
            if current_total + value / 2.0 > target_total:
                rows.append(current)
                current = [value]
                current_total = value
            else:
                current.append(value)
                current_total += value
        rows = self._append_to_rows(rows, current, n_rows)
        while len(rows) < n_rows:
            rows.append([])
        return rows

    def _get_rectangles(self, values, total):
        if not values or total <= 0:
            return []
        n_rows = max(1, round(len(values) ** 0.5))
        rows = self._split_rows(values, n_rows)
        rows = [row for row in rows if row]
        rectangles = []
        y = 0.0
        for row in rows:
            row_total = sum(row) or 1.0
            row_height = row_total / total * (1.0 - self.RECT_GAP)
            x = 0.0
            for value in row:
                width = value / row_total * (1.0 - self.RECT_GAP)
                rectangles.append((x, y, width, row_height, value))
                x += width + self.RECT_GAP
            y += row_height + self.RECT_GAP
        return rectangles
