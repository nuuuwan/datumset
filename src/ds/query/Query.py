from dataclasses import dataclass
from functools import cache, cached_property


@dataclass(frozen=True)
class Query:
    query_str: str

    DELIM_PART = "/"
    OPR_ADD = "+"
    OPR_MULT = "*"
    OPR_EQ = "="
    OPR_LT = "<"
    OPR_OR = ","

    def _is_child_region_spec(self, dim_spec):
        return self.OPR_LT in dim_spec and self.OPR_EQ in dim_spec

    def _get_dim_label(self, dim_spec):
        if self.OPR_LT in dim_spec:
            dim_spec = dim_spec.split(self.OPR_LT, 1)[0]
        if self.OPR_EQ in dim_spec:
            return dim_spec.split(self.OPR_EQ, 1)[0]
        return dim_spec

    @cached_property
    def parts(self):
        return self.query_str.split(self.DELIM_PART)

    # ---

    @cached_property
    def entity_part(self):
        return self.parts[0]

    @cached_property
    def dim_part(self):
        return self.parts[1]

    @cached_property
    def cell_part(self):
        return self.parts[2]

    # ---

    @cached_property
    def entity_class_names(self):
        return self.entity_part.split(self.OPR_ADD)

    @cached_property
    def dim_specs(self):
        return self.dim_part.split(self.OPR_MULT)

    @cached_property
    def dim_labels(self):
        return [self._get_dim_label(dim_spec) for dim_spec in self.dim_specs]

    @cached_property
    def dim_values_idx(self):
        dim_values_idx = {}
        for dim_spec in self.dim_specs:
            if self._is_child_region_spec(dim_spec):
                continue
            if self.OPR_EQ not in dim_spec:
                continue
            dim_label, dim_value = dim_spec.split(self.OPR_EQ, 1)
            dim_values_idx[dim_label] = dim_value
        return dim_values_idx

    @cached_property
    def cell_labels(self):
        return self.cell_part.split(self.OPR_MULT)

    @cached_property
    def base_query_str(self):
        return self.from_parts(
            tuple(self.entity_class_names),
            tuple(self.dim_labels),
            tuple(self.cell_labels),
        ).query_str

    # ---
    @classmethod
    @cache
    def from_parts(cls, entity_class_names, dim_labels, cell_labels):
        entity_part = cls.OPR_ADD.join(entity_class_names)
        dim_part = cls.OPR_MULT.join(dim_labels)
        cell_part = cls.OPR_MULT.join(cell_labels)
        query_str = cls.DELIM_PART.join([entity_part, dim_part, cell_part])
        return cls(query_str)
