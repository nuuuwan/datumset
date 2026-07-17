from ds.query.Query import Query
from utils_future import Log

log = Log("DatumMatchMixin")


class DatumMatchMixin:
    def is_match_entity(self, entity_part: str) -> bool:
        entity_class_names = entity_part.split(Query.OPR_ADD)
        for entity_class_name in entity_class_names:
            if self.entity_class.__name__ == entity_class_name:
                return entity_class_name
        return False

    def is_match_dim_idx(self, concept_part: str) -> bool:
        dim_labels = list(self.dim_idx.keys())
        labels_required = concept_part.split(Query.OPR_MULT)
        if labels_required != dim_labels:
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
            and self.is_match_dim_idx(query.concept_part)
            and self.is_match_cell_idx(query.cell_part)
        )
