from ds.thing.concept.CategoryConcept import CategoryConcept
from ds.thing.concept.region.Region import Region
from ds.thing.concept.Time import Time


class VisualParamsMixin:

    def _get_dim_concept(self, dim_key):
        return self.datumset[0].dim_idx.get(dim_key)

    def _can_shorten_dim(self, dim_key):
        concept = self._get_dim_concept(dim_key)
        if isinstance(concept, CategoryConcept):
            return type(concept).can_shorten()
        return True

    def _get_ordered_category_valid_values(self, dim_key):
        concept = self._get_dim_concept(dim_key)
        if not isinstance(concept, CategoryConcept):
            return None
        concept_cls = type(concept)
        if not concept_cls.is_ordered():
            return None
        return concept_cls.valid_values()

    def _is_region_dim(self, dim_key):
        return isinstance(self._get_dim_concept(dim_key), Region)

    def _is_time_dim(self, dim_key):
        return isinstance(self._get_dim_concept(dim_key), Time)

    def _get_x_dim_key(self):
        varying = self._get_varying_dim_keys()
        for dim_key in varying:
            if self._is_time_dim(dim_key):
                return dim_key
        return varying[-1]

    def _get_region_dim_key(self):
        for dim_key in self._get_dim_labels():
            if self._is_region_dim(dim_key):
                return dim_key
        raise ValueError(
            "No region dimension key found in datumset."
        )  # pragma: no cover

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
            for dim_key in self._get_varying_dim_keys()
            if dim_key not in excluded_dim_keys
        ]
        self.split_dims = split_dims
        if not split_dims:
            return [self.datumset]
        datumsets = self.datumset.split(*split_dims)
        return self._sort_display_datumsets(datumsets, split_dims)

    def _sort_display_datumsets(self, datumsets, split_dims):
        def sort_key(datumset):
            return tuple(
                datumset[0].dim_idx[dim_key].get_value()
                for dim_key in split_dims
            )

        return sorted(datumsets, key=sort_key)

    def _get_unique_dim_values(self, dim_key):
        values = []
        for datum in self.datumset:
            value = datum.dim_idx[dim_key].get_value()
            if value not in values:
                values.append(value)
        return values
