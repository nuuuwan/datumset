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

    def is_match_time(self, time_part: str) -> bool:
        time_values = time_part.split(Query.OPR_ADD)
        for time_value in time_values:
            if self.time.is_match(time_value):
                return time_value
        return False

    def get_concept_labels(self) -> set[str]:
        return set(self.concept_idx.keys())

    def is_match_concept_idx(self, concept_part: str) -> bool:
        labels_required = set(concept_part.split(Query.OPR_MULT))
        if labels_required != self.get_concept_labels():
            return False
        return True

    def is_match(self, query: Query) -> bool:
        time_part = self.is_match_time(query.time_part)
        entity_part = self.is_match_entity(query.entity_part)
        concept_part = self.is_match_concept_idx(query.concept_part)
        if not (time_part and entity_part and concept_part):
            return None
        return dict(
            entity=entity_part,
            time=time_part,
            concept=concept_part,
        )
