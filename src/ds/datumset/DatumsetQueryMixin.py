from propcache import cached_property

from ds.query.Query import Query


class DatumsetQueryMixin:

    def _get_entity_class_names(self):
        entity_class_names = []
        for datum in self._value:
            if datum.entity_class.__name__ not in entity_class_names:
                entity_class_names.append(datum.entity_class.__name__)
        return entity_class_names

    def _get_time_values(self):
        time_values = []
        for datum in self._value:
            if datum.time.get_value() not in time_values:
                time_values.append(datum.time.get_value())
        return time_values

    def _get_concept_labels(self):
        concept_labels = []
        for datum in self._value:
            for label in datum.get_concept_labels():
                if label not in concept_labels:
                    concept_labels.append(label)
        return concept_labels

    def _infer_query(self) -> Query:
        query = Query.from_parts(
            self._get_time_values(),
            self._get_entity_class_names(),
            self._get_concept_labels(),
        )
        return query

    @cached_property
    def query(self):
        return self._infer_query()
