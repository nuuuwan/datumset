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


class Datumset(
    DatumsetSerializeMixin,
    DatumsetBase,
    DatumsetSplitMixin,
):
    pass
