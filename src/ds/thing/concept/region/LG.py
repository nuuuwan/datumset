from functools import cache

from utils_future import JSONFile

from ds.thing.concept.region.Region import Region


class LG(Region):

    @staticmethod
    @cache
    def get_lg_corrections():
        idx = JSONFile(
            "src", "ds", "thing", "concept", "region", "lg.corrections.json"
        ).read()
        inverse_idx = {v: k for k, v in idx.items()}
        return inverse_idx

    @classmethod
    @cache
    def list(cls):
        r_list = Region.list.__func__(cls)
        lg_corrections = cls.get_lg_corrections()
        new_r_list = []
        for r in r_list:
            new_r = cls(
                id=lg_corrections.get(r.id, r.id),
                name=r.name,
            )
            new_r_list.append(new_r)
        return new_r_list
