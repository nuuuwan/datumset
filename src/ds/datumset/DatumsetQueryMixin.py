from propcache import cached_property

from ds.query.Query import Query


class DatumsetQueryMixin:

    @cached_property
    def query(self):
        return self._infer_query()

    def _infer_query(self) -> Query:
        entity_class_names = []
        time_values = []
        concept_labels = []

        for datum in self._value:
            if datum.entity_class.__name__ not in entity_class_names:
                entity_class_names.append(datum.entity_class.__name__)
            if datum.time.get_value() not in time_values:
                time_values.append(datum.time.get_value())
            for label in datum.get_concept_labels():
                if label not in concept_labels:
                    concept_labels.append(label)

        query = Query.from_parts(
            time_values,
            entity_class_names,
            concept_labels,
        )
        return query
