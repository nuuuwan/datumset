from abc import ABC


class Measurement(ABC):
    @classmethod
    def is_match(cls, query_str):
        return query_str == cls.__name__
