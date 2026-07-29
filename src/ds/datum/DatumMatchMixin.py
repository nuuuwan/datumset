from ds.datum.DatumMatchRegionMixin import DatumMatchRegionMixin
from ds.query.Query import Query


class DatumMatchMixin(DatumMatchRegionMixin):

    def _is_match_required_value(self, dim_label, required_value):
        dim_value = str(self.dim_idx[dim_label].get_value()).lower()
        if isinstance(required_value, tuple):
            return dim_value in required_value
        return dim_value == str(required_value).lower()

    def is_match_entity(self, entity_part: str) -> bool:
        entity_class_names = entity_part.split(Query.OPR_ADD)
        for entity_class_name in entity_class_names:
            if self.entity_class.__name__ == entity_class_name:
                return entity_class_name
        return False

    def is_match_dim_idx(self, concept_part: str) -> bool:
        dim_labels = list(self.dim_idx.keys())
        labels_required, values_required = self._parse_dim_part(concept_part)
        if labels_required != dim_labels:
            return False
        for dim_label, required_value in values_required.items():
            if not self._is_match_required_value(dim_label, required_value):
                return False
        return True

    def is_match_cell_idx(self, cell_part: str) -> bool:
        cell_labels = list(self.cell_idx.keys())
        labels_required = cell_part.split(Query.OPR_MULT)
        if labels_required != cell_labels:
            return False
        return True

    def is_match(self, query: Query) -> bool:
        return (
            self.is_match_entity(query.entity_part)
            and self.is_match_dim_idx(query.dim_part)
            and self.is_match_cell_idx(query.cell_part)
        )
