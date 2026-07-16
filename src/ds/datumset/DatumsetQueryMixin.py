from propcache import cached_property

from ds.query.Query import Query


class DatumsetQueryMixin:

    @cached_property
    def query(self):
        return self.infer_query()

    def infer_query(self) -> Query:
        entity_class_names = set()
        time_values = set()
        concept_labels = set()

        for datum in self._value:
            entity_class_names.add(datum.entity_class.__name__)
            time_values.add(datum.time.get_value())
            concept_labels.update(datum.get_concept_labels())

        return Query.from_parts(
            sorted(time_values),
            sorted(entity_class_names),
            sorted(concept_labels),
        )
