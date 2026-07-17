from propcache import cached_property

from ds.query.Query import Query


class DatumsetQueryMixin:

    def _get_entity_class_names(self):
        entity_class_names = []
        for datum in self._value:
            if datum.entity_class.__name__ not in entity_class_names:
                entity_class_names.append(datum.entity_class.__name__)
        return entity_class_names

    def _get_dim_labels(self):
        dim_labels = []
        for datum in self._value:
            for dim_label in datum.dim_idx.keys():
                if dim_label not in dim_labels:
                    dim_labels.append(dim_label)
        return dim_labels

    def _get_cell_labels(self):
        cell_labels = []
        for datum in self._value:
            for cell_label in datum.cell_idx.keys():
                if cell_label not in cell_labels:
                    cell_labels.append(cell_label)
        return cell_labels

    def _infer_query(self) -> Query:
        query = Query.from_parts(
            self._get_entity_class_names(),
            self._get_dim_labels(),
            self._get_cell_labels(),
        )
        return query

    @cached_property
    def query(self):
        return self._infer_query()
