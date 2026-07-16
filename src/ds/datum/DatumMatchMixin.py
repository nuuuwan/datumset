from ds.query.Query import Query


class DatumMatchMixin:
    def is_match_entity(self, entity_part: str) -> bool:
        entity_class_names = entity_part.split(Query.OPR_ADD)
        for entity_class_name in entity_class_names:
            if self.entity_class.__name__ == entity_class_name:
                return entity_class_name
        return None

    def is_match_time(self, time_part: str) -> bool:
        time_values = time_part.split(Query.OPR_ADD)
        for time_value in time_values:
            if self.time.is_match(time_value):
                return time_value
        return None

    def is_match_concept_idx(self, concept_part: str) -> bool:
        class_names_required = concept_part.split(Query.OPR_MULT)
        matches = {}
        for class_name in class_names_required:
            has_match = False
            for concept_key, concept in self.concept_idx.items():
                if concept.is_match(class_name):
                    has_match = True
                    matches[concept_key] = class_name
                    break
            if not has_match:
                return None
        return matches

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
