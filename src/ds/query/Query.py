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
    def measurement_part(self):
        return self.parts[2]

    @cached_property
    def entity_list(self):
        return self.entity_part.split(self.OPR_ADD)

    @cached_property
    def time_list(self):
        return self.time_part.split(self.OPR_ADD)

    @cached_property
    def measurement_list(self):
        return self.measurement_part.split(self.OPR_MULT)

    @classmethod
    def from_metadata(cls, metadata):
        entity = metadata['entity']
        time = metadata['time']
        measurement = metadata['measurement']

        return cls(
            query_str=Query.DELIM_PART.join(
                [
                    Query.OPR_ADD.join(entity),
                    Query.OPR_ADD.join(time),
                    Query.OPR_MULT.join(measurement.values()),
                ]
            )
        )
