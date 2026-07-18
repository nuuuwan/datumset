from ds.thing.concept.Concept import Concept


class Bool(Concept):
    @classmethod
    def from_value(cls, value):
        return cls(bool(value))
