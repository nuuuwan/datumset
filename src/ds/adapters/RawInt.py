class RawInt:
    def __init__(self, v):
        self._v = int(v)

    def to_kvpair(self):
        return self._v

    def __hash__(self):
        return hash(self._v)

    def __eq__(self, other):
        if isinstance(other, RawInt):
            return self._v == other._v
        return NotImplemented
