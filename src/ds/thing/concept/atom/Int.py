from ds.thing.concept.Concept import Concept


class Int(Concept):
    @classmethod
    def from_value(cls, value):
        return cls(int(value))
