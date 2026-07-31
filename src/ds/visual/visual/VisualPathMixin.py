from functools import cached_property

from utils_future import Directory, File

from ds.query.Query import Query


class VisualPathMixin:

    def _get_path_cell_part(self):
        source_query_str = getattr(self.datumset, "_query_str", None)
        if source_query_str:
            return Query(source_query_str).cell_part
        return self.datumset[0].query.cell_part

    def _get_query_str_for_path(self):
        source_query_str = getattr(self.datumset, "_query_str", None)
        if source_query_str:
            return source_query_str
        query = self.datumset[0].query
        return Query.DELIM_PART.join(
            [
                query.entity_part,
                query.dim_part,
                self._get_path_cell_part(),
            ]
        )

    @cached_property
    def dir_visual(self) -> Directory:
        query_str_for_path = self._get_query_str_for_path()
        dir_visual = Directory("images", query_str_for_path)
        dir_visual.make()
        return dir_visual

    @cached_property
    def image_file(self) -> File:
        return File(self.dir_visual, self.__class__.__name__ + ".png")
