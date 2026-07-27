from functools import cache

from utils_future import Log

from ds.query.Query import Query
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.region.RegionMatcher import RegionMatcher

log = Log("DatumMatchMixin")


class DatumMatchMixin:

    @cache
    def _is_child_region_spec(self, dim_spec: str) -> bool:
        return Query.OPR_LT in dim_spec and Query.OPR_EQ in dim_spec

    @cache
    def _get_child_region_values(self, child_dim_label, parent_spec):
        parent_dim_label, parent_dim_value = parent_spec.split(
            Query.OPR_EQ, 1
        )
        child_region_class = RegionFactory[child_dim_label]
        parent_region_class = RegionFactory[parent_dim_label]
        parent_region = parent_region_class[parent_dim_value]
        child_regions = RegionMatcher.get_child_regions(
            parent_region,
            child_region_class,
        )
        return tuple(
            sorted(
                child_region.get_value().lower()
                for child_region in child_regions
            )
        )

    @cache
    def _is_match_required_value(self, dim_label, required_value):
        dim_value = str(self.dim_idx[dim_label].get_value()).lower()
        if isinstance(required_value, tuple):
            return dim_value in required_value
        return dim_value == str(required_value).lower()

    @cache
    def _parse_dim_part(
        self, concept_part: str
    ) -> tuple[list[str], dict[str, str | tuple[str, ...]]]:
        labels_required = []
        values_required = {}
        for dim_spec in concept_part.split(Query.OPR_MULT):
            if self._is_child_region_spec(dim_spec):
                child_dim_label, parent_spec = dim_spec.split(
                    Query.OPR_LT,
                    1,
                )
                labels_required.append(child_dim_label)
                values_required[child_dim_label] = (
                    self._get_child_region_values(
                        child_dim_label,
                        parent_spec,
                    )
                )
                continue
            if Query.OPR_EQ in dim_spec:
                dim_label, dim_value = dim_spec.split(Query.OPR_EQ, 1)
                labels_required.append(dim_label)
                values_required[dim_label] = dim_value
                continue
            labels_required.append(dim_spec)
        return labels_required, values_required

    @cache
    def is_match_entity(self, entity_part: str) -> bool:
        entity_class_names = entity_part.split(Query.OPR_ADD)
        for entity_class_name in entity_class_names:
            if self.entity_class.__name__ == entity_class_name:
                return entity_class_name
        return False

    @cache
    def is_match_dim_idx(self, concept_part: str) -> bool:
        dim_labels = list(self.dim_idx.keys())
        labels_required, values_required = self._parse_dim_part(concept_part)
        if labels_required != dim_labels:
            return False
        for dim_label, required_value in values_required.items():
            if not self._is_match_required_value(dim_label, required_value):
                return False
        return True

    @cache
    def is_match_cell_idx(self, cell_part: str) -> bool:
        cell_labels = list(self.cell_idx.keys())
        labels_required = cell_part.split(Query.OPR_MULT)
        if labels_required != cell_labels:
            return False
        return True

    @cache
    def is_match(self, query: Query) -> bool:
        return (
            self.is_match_entity(query.entity_part)
            and self.is_match_dim_idx(query.dim_part)
            and self.is_match_cell_idx(query.cell_part)
        )
