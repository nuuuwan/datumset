from ds.thing.ThingFactory import ThingFactory
from utils_future import ShallowDict


class DatumSerializeMixin:
    def to_data(self):
        nesting_values = [
            self.entity_class.__name__,
        ] + list([v.to_kvpair() for v in self.dim_idx.values()])
        shallow_dict = ShallowDict()
        shallow_dict[tuple(nesting_values)] = {
            k: v.to_kvpair() for k, v in self.cell_idx.items()
        }
        return shallow_dict.to_deep()

    @classmethod
    def from_data(cls, data):
        key_parts = []
        node = data
        while isinstance(node, dict) and any(
            isinstance(v, dict) for v in node.values()
        ):
            k, node = next(iter(node.items()))
            key_parts.append(k)
        entity_class = ThingFactory[key_parts[0]]
        dim_idx = {
            kv.split(":")[0]: ThingFactory.from_kvpair(kv)
            for kv in key_parts[1:]
        }
        cell_idx = {k: ThingFactory.from_kvpair(v) for k, v in node.items()}
        return cls(entity_class, dim_idx, cell_idx)
