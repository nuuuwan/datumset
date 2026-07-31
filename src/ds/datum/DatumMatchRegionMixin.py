from functools import cache

from ds.query.Query import Query
from ds.thing.concept.region.RegionFactory import RegionFactory
from ds.thing.concept.region.RegionMatcher import RegionMatcher


class DatumMatchRegionMixin:

    @staticmethod
    @cache
    def _is_child_region_spec(dim_spec: str) -> bool:
        return Query.OPR_LT in dim_spec and Query.OPR_EQ in dim_spec

    @staticmethod
    @cache
    def _get_child_region_values(child_dim_label, parent_spec):
        parent_dim_label, parent_dim_value = parent_spec.split(
            Query.OPR_EQ, 1
        )
        child_region_class = RegionFactory[child_dim_label]
        parent_region_class = RegionFactory[parent_dim_label]
        values = set()
        for parent_value in parent_dim_value.split(Query.OPR_OR):
            child_regions = RegionMatcher.get_child_regions(
                parent_region_class[parent_value],
                child_region_class,
            )
            values.update(
                child_region.get_value().lower()
                for child_region in child_regions
            )
        return tuple(sorted(values))

    @staticmethod
    @cache
    def _parse_dim_value(dim_value: str):
        if Query.OPR_OR in dim_value:
            return tuple(
                value.lower() for value in dim_value.split(Query.OPR_OR)
            )
        return dim_value

    @staticmethod
    @cache
    def _parse_dim_part(
        concept_part: str,
    ) -> tuple[list[str], dict[str, str | tuple[str, ...]]]:
        labels_required = []
        values_required = {}
        for dim_spec in concept_part.split(Query.OPR_ADD):
            if DatumMatchRegionMixin._is_child_region_spec(dim_spec):
                child_dim_label, parent_spec = dim_spec.split(
                    Query.OPR_LT,
                    1,
                )
                labels_required.append(child_dim_label)
                values_required[child_dim_label] = (
                    DatumMatchRegionMixin._get_child_region_values(
                        child_dim_label,
                        parent_spec,
                    )
                )
                continue
            if Query.OPR_EQ in dim_spec:
                dim_label, dim_value = dim_spec.split(Query.OPR_EQ, 1)
                labels_required.append(dim_label)
                values_required[dim_label] = (
                    DatumMatchRegionMixin._parse_dim_value(dim_value)
                )
                continue
            labels_required.append(dim_spec)
        return labels_required, values_required
