from collections import defaultdict

from ds.lanka_data.LankaData import LankaData
from ds.thing.concept.Time import Time


class MapVisualPercentMixin:

    def _total_dim_spec(self, dim_label):
        if dim_label == self.region_dim_key:
            return dim_label
        if isinstance(self._get_dim_concept(dim_label), Time):
            value = self.datumset[0].dim_idx[dim_label].get_value()
            return f"{dim_label}={value}"
        return dim_label

    def _get_total_query_str(self):
        query = self.datumset[0].query
        specs = [
            self._total_dim_spec(dim_label) for dim_label in query.dim_labels
        ]
        return "/".join([query.entity_part, "*".join(specs), query.cell_part])

    def _get_datum_dim_key(self, datum):
        return tuple(
            sorted((k, v.get_value()) for k, v in datum.dim_idx.items())
        )

    def _get_region_totals(self):
        total_datumset = LankaData[self._get_total_query_str()]
        seen = {}
        for datum in total_datumset:
            seen[self._get_datum_dim_key(datum)] = datum
        totals = defaultdict(float)
        for datum in seen.values():
            region = self._normalize_region_key(
                datum.dim_idx[self.region_dim_key].get_value()
            )
            totals[region] += float(
                datum.cell_idx[self.y_cell_key].get_value()
            )
        return totals

    def _get_region_percentages(self, sub_datumset):
        values = self._get_region_values_for(sub_datumset)
        totals = self._get_region_totals()
        return {
            region: value / totals[region]
            for region, value in values.items()
            if totals.get(region)
        }
