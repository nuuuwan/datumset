from ds.thing.concept.region.Region import Region


class VisualParamsMixin:

    def _get_dim_concept(self, dim_key):
        return self.datumset[0].dim_idx.get(dim_key)

    def _is_region_dim(self, dim_key):
        return isinstance(self._get_dim_concept(dim_key), Region)

    def _get_region_dim_key(self):
        for dim_key in self._get_dim_labels():
            if self._is_region_dim(dim_key):
                return dim_key
        raise ValueError("No region dimension key found in datumset.")

    def _get_y_cell_key(self):
        # TODO: At the moment, everything is "Count",
        # but this should change.
        return "Count"

    def _get_varying_dim_keys(self) -> list[str]:
        return self.datumset.get_non_singleton_dims()

    def _get_dim_labels(self):
        return self.datumset[0].query.dim_labels

    def _get_display_datumsets(self, excluded_dim_keys):
        split_dims = [
            dim_key
            for dim_key in self._get_dim_labels()
            if dim_key not in excluded_dim_keys
        ]
        print(f"{split_dims=}")
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
