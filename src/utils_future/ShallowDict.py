from collections.abc import MutableMapping


class ShallowDict(MutableMapping):

    def __init__(self, initial_dict=None):
        self._dict = initial_dict or {}

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        for existing in list(self._dict.keys()):
            n = min(len(key), len(existing))
            if existing[:n] == key[:n]:
                del self._dict[existing]
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def to_deep(self):
        result = {}
        for keys, value in self._dict.items():
            node = result
            for key in keys[:-1]:
                node = node.setdefault(key, {})
            node[keys[-1]] = value
        return result

    @classmethod
    def from_deep(cls, nested_dict):
        flat = {}

        def _recurse(node, path):
            if not isinstance(node, dict):
                flat[tuple(path)] = node
                return
            for key, child in node.items():
                _recurse(child, path + [key])

        _recurse(nested_dict, [])
        return cls(flat)

    def __eq__(self, other):
        if isinstance(other, ShallowDict):
            return self.to_deep() == other.to_deep()
        return NotImplemented

    def __add__(self, other):
        if not isinstance(other, ShallowDict):
            return NotImplemented
        new_dict = self._dict.copy()
        new_dict.update(other._dict)
        return ShallowDict(new_dict)
