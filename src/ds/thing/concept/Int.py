from ds.thing.concept.Concept import Concept


class Int(Concept):
    pass

    def to_kvpair(self):
        return int(self._value)
