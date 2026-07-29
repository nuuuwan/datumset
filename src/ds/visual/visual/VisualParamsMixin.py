from ds.thing.concept.region.Region import Region


class VisualParamsMixin:

    def _get_query(self):
        return self.datumset[0].query

    def _get_dim_concept(self, dim_key):
        return self.datumset[0].dim_idx.get(dim_key)

    def _is_region_dim(self, dim_key):
        return isinstance(self._get_dim_concept(dim_key), Region)

    def _get_region_dim_key(self):
        for dim_key in self._get_dim_labels():
            if self._is_region_dim(dim_key):
                return dim_key
        return self._get_dim_labels()[0]

    def _get_y_cell_key(self):
        cell_labels = self._get_query().cell_labels
        for cell_label in cell_labels:
            if cell_label == "Count":
                return cell_label
        return cell_labels[0]

    def _get_varying_dim_keys(self, excluded_dim_keys=None):
        excluded_dim_keys = excluded_dim_keys or set()
        varying = []
        for dim_key in self._get_dim_labels():
            if dim_key in excluded_dim_keys:
                continue
            if len(self._get_unique_dim_values(dim_key)) > 1:
                varying.append(dim_key)
        return varying

    def _get_first_varying_dim_key(self, excluded_dim_keys=None):
        varying = self._get_varying_dim_keys(excluded_dim_keys)
        if varying:
            return varying[0]
        return self._get_dim_labels()[0]

    def _get_first_varying_non_region_dim_key(self):
        for dim_key in self._get_varying_dim_keys():
            if not self._is_region_dim(dim_key):
                return dim_key
        return self._get_first_varying_dim_key()

    def _get_dim_labels(self):
        return self.datumset[0].query.dim_labels

    def _get_display_datumsets(self, excluded_dim_keys):
        split_dims = [
            dim_key
            for dim_key in self._get_dim_labels()
            if dim_key not in excluded_dim_keys
        ]
        if not split_dims:
            return [self.datumset]
        return self.datumset.split(*split_dims)

    def _get_unique_dim_values(self, dim_key):
        values = []
        for datum in self.datumset:
            value = datum.dim_idx[dim_key].get_value()
            if value not in values:
                values.append(value)
        return values
