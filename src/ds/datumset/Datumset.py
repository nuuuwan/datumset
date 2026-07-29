from ds.datumset.DatumsetBase import DatumsetBase
from ds.datumset.DatumsetSerializeMixin import DatumsetSerializeMixin


class DatumsetSplitMixin:

    def split(self, *split_dims: list[str]) -> list["Datumset"]:
        idx = {}
        for datum in self:
            key_items = []
            for split_dim in split_dims:
                split_dim_value = datum.dim_idx[split_dim]
                key_items.append(f"{split_dim}:{split_dim_value}")
            key = "/".join(key_items)
            if key not in idx:
                idx[key] = []
            idx[key].append(datum)

        datumset_list = []
        for datum_list_for_key in idx.values():
            datumset_list.append(Datumset(*datum_list_for_key))
        return datumset_list

    def get_dim_to_values(self) -> dict[str, set]:
        dim_to_values = {}
        for datum in self:
            for dim_key, dim_value in datum.dim_idx.items():
                if dim_key not in dim_to_values:
                    dim_to_values[dim_key] = set()
                dim_to_values[dim_key].add(dim_value)
        return dim_to_values

    def get_singleton_dims(self) -> set[str]:
        dim_to_values = self.get_dim_to_values()
        singleton_dims = set()
        for dim_key, values in dim_to_values.items():
            if len(values) == 1:
                singleton_dims.add(dim_key)
        return singleton_dims

    def get_non_singleton_dims(self) -> set[str]:
        dim_to_values = self.get_dim_to_values()
        non_singleton_dims = set()
        for dim_key, values in dim_to_values.items():
            if len(values) > 1:
                non_singleton_dims.add(dim_key)
        return non_singleton_dims


class Datumset(
    DatumsetSerializeMixin,
    DatumsetBase,
    DatumsetSplitMixin,
):
    pass
