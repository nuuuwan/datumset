from ds.thing.concept.Concept import Concept


class Float(Concept):
    @classmethod
    def from_value(cls, value):
        return cls(float(value))
