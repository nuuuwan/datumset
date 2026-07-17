from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Query:
    query_str: str

    DELIM_PART = "/"
    OPR_ADD = "+"
    OPR_MULT = "*"

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
    def dim_labels(self):
        return self.dim_part.split(self.OPR_MULT)

    @cached_property
    def cell_labels(self):
        return self.cell_part.split(self.OPR_MULT)

    # ---
    @classmethod
    def from_parts(cls, entity_class_names, dim_labels, cell_labels):
        entity_part = cls.OPR_ADD.join(entity_class_names)
        dim_part = cls.OPR_MULT.join(dim_labels)
        cell_part = cls.OPR_MULT.join(cell_labels)
        query_str = cls.DELIM_PART.join([entity_part, dim_part, cell_part])
        return cls(query_str)
