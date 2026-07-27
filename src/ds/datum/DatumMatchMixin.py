from functools import cache

from utils_future import Log

from ds.query.Query import Query

log = Log("DatumMatchMixin")


class DatumMatchMixin:

    @cache
    def _parse_dim_part(
        self, concept_part: str
    ) -> tuple[list[str], dict[str, str]]:
        labels_required = []
        values_required = {}
        for dim_spec in concept_part.split(Query.OPR_MULT):
            if Query.OPR_EQ in dim_spec:
                dim_label, dim_value = dim_spec.split(Query.OPR_EQ, 1)
                labels_required.append(dim_label)
                values_required[dim_label] = dim_value
                continue
            labels_required.append(dim_spec)
        return labels_required, values_required

    @cache
    def _is_match_dim_values(self, values_required_key: str) -> bool:
        if not values_required_key:
            return True
        for dim_value_required_spec in values_required_key.split(
            Query.OPR_MULT
        ):
            dim_label, dim_value_required = dim_value_required_spec.split(
                Query.OPR_EQ,
                1,
            )
            dim_value = self.dim_idx[dim_label].get_value()
            if str(dim_value).lower() != dim_value_required.lower():
                return False
        return True

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
        values_required_key = Query.OPR_MULT.join(
            [
                f"{dim_label}{Query.OPR_EQ}{dim_value}"
                for dim_label, dim_value in values_required.items()
            ]
        )
        if not self._is_match_dim_values(values_required_key):
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
