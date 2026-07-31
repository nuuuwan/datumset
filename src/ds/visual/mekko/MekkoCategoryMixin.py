from collections import defaultdict


class MekkoCategoryMixin:

    OTHER_CATEGORY_SUFFIX = "Other {category}"
    OTHER_CATEGORY_TOKEN = "_other_{category}"
    SMALL_CATEGORY_THRESHOLD = 0.01
    MIN_CATEGORY_COUNT = 7

    def _get_other_category(self):
        return self.OTHER_CATEGORY_TOKEN.format(category=self.x_dim_key)

    def _compute_mekko_small_x_labels(self, sub_datumset):
        x_labels, _, data = self._get_data(sub_datumset)
        totals = self._get_totals(x_labels, data)
        grand_total = sum(totals) or 1.0
        if len(x_labels) <= self.MIN_CATEGORY_COUNT:
            return set()
        return {
            x_label
            for x_label, total in zip(x_labels, totals)
            if total / grand_total < self.SMALL_CATEGORY_THRESHOLD
        }

    def _remap_x_label(self, x_label, small_x_labels):
        if x_label in small_x_labels:
            return self._get_other_category()
        return x_label

    def _format_mekko_x_label(self, x_label):
        other_category = self._get_other_category()
        if x_label == other_category:
            return self.OTHER_CATEGORY_SUFFIX.format(category=self.x_dim_key)
        return self._format_visual_value(x_label)

    def _build_remapped_data(self, x_labels, stack_labels, data, small_x):
        remapped_x_labels = []
        remapped_data = defaultdict(dict)
        for x_label in x_labels:
            remapped = self._remap_x_label(x_label, small_x)
            if remapped not in remapped_x_labels:
                remapped_x_labels.append(remapped)
            for stack_label in stack_labels:
                value = data[stack_label].get(x_label, 0.0)
                remapped_data[stack_label][remapped] = (
                    remapped_data[stack_label].get(remapped, 0.0) + value
                )
        return remapped_x_labels, remapped_data

    def _get_mekko_data(self, sub_datumset):
        x_labels, stack_labels, data = self._get_data(sub_datumset)
        small_x_labels = self._compute_mekko_small_x_labels(sub_datumset)
        if not small_x_labels:
            return x_labels, stack_labels, data
        remapped_x_labels, remapped_data = self._build_remapped_data(
            x_labels,
            stack_labels,
            data,
            small_x_labels,
        )
        return remapped_x_labels, stack_labels, remapped_data
