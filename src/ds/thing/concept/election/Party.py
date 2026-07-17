from ds.thing.concept.Concept import Concept


class Party(Concept):
    RAW_COLUMNS = True

    @classmethod
    def __class_getitem__(cls, value):
        return cls(value)

    @classmethod
    def from_value(cls, value):
        return cls(value)
