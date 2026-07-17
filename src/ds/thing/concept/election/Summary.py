from ds.thing.concept.Concept import Concept


class Summary(Concept):
    @classmethod
    def __class_getitem__(cls, value):
        return cls(value)

    @classmethod
    def from_value(cls, value):
        return cls(value)
