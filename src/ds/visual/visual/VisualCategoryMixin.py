from collections import defaultdict
from functools import cached_property


class VisualCategoryMixin:

    def _compute_small_categories(self):
        dim_key = self._get_category_dim_key()
        if dim_key is None:
            return set()
        cell_key = self._get_y_cell_key()
        totals = defaultdict(float)
        for datum in self.datumset:
            category = datum.dim_idx[dim_key].get_value()
            totals[category] += float(datum.cell_idx[cell_key].get_value())
        grand_total = sum(totals.values()) or 1.0
        return {
            category
            for category, total in totals.items()
            if total / grand_total < self.SMALL_CATEGORY_THRESHOLD
        }

    @cached_property
    def _small_categories(self):
        return self._compute_small_categories()

    def _remap_category(self, value):
        if value in self._small_categories:
            return self.OTHER_CATEGORY
        return value

    def _get_category_values(self, dim_key):
        values = []
        for datum in self.datumset:
            value = self._remap_category(datum.dim_idx[dim_key].get_value())
            if value not in values:
                values.append(value)
        return values

    def _init_category_colors(self, dim_key):
        dim_values = self._get_category_values(dim_key)
        color_idx = self._get_dim_color_idx(dim_key, dim_values)
        return dim_values, color_idx

    def _init_dim_colors(self, dim_key):
        dim_values = self._get_unique_dim_values(dim_key)
        color_idx = self._get_dim_color_idx(dim_key, dim_values)
        return dim_values, color_idx
