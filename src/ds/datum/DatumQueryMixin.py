from propcache import cached_property

from ds.query.Query import Query


class DatumQueryMixin:

    def _infer_query(self) -> Query:
        query = Query.from_parts(
            self.entity_class.__name__,
            tuple(self.dim_idx.keys()),
            tuple(self.cell_idx.keys()),
        )
        return query

    @cached_property
    def query(self):
        return self._infer_query()
