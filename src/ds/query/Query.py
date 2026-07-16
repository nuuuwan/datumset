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
    def time_values(self):
        return self.time_part.split(self.OPR_ADD)

    @cached_property
    def entity_class_names(self):
        return self.entity_part.split(self.OPR_ADD)

    @cached_property
    def concept_class_names(self):
        return self.concept_part.split(self.OPR_MULT)

    def normalize(self):
        time_values = sorted(self.time_values)
        entity_class_names = sorted(self.entity_class_names)
        concept_class_names = sorted(self.concept_class_names)

        normalized_query_str = self.DELIM_PART.join(
            [
                self.OPR_ADD.join(entity_class_names),
                self.OPR_ADD.join(time_values),
                self.OPR_MULT.join(concept_class_names),
            ]
        )
        return Query(normalized_query_str)
