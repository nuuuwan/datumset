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

    @cached_property
    def entity_part(self):
        return self.parts[0]

    @cached_property
    def time_part(self):
        return self.parts[1]

    @cached_property
    def concept_part(self):
        return self.parts[2]

    @cached_property
    def entity_list(self):
        return self.entity_part.split(self.OPR_ADD)

    @cached_property
    def time_list(self):
        return self.time_part.split(self.OPR_ADD)

    @cached_property
    def concept_list(self):
        return self.concept_part.split(self.OPR_MULT)

    @classmethod
    def from_data(cls, query_str):
        return cls(query_str=query_str)

    def to_data(self):
        return self.query_str
