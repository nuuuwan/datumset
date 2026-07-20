from dataclasses import dataclass
from functools import cache

from utils_future import WWW, Directory, File, JSONFile

from ds.thing.concept.CategoryConcept import CategoryConcept


@dataclass(frozen=True)
class Region(CategoryConcept):
    id: str
    name: str

    def __init__(self, id: str, name: str):
        object.__setattr__(self, "_value", id)
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)

    @classmethod
    def region_class_id(cls):
        return cls.__name__.lower()

    @classmethod
    @cache
    def valid_values(cls):
        return [r.id for r in cls.list()]

    @classmethod
    @cache
    def list(cls):
        data_file = JSONFile(
            Directory.get_temp("datumset", "regions").path,
            f"{cls.region_class_id()}s.json",
        )
        url = (
            "https://raw.githubusercontent.com"
            + "/nuuuwan"
            + "/lk_admin_regions/refs/heads/main"
            + f"/data/ents/{cls.region_class_id()}s.json"
        )
        WWW(url).download(File(data_file.path))
        data_list = data_file.read()
        return [cls(id=d["id"], name=d["name"]) for d in data_list]

    @classmethod
    @cache
    def from_value(cls, value: str):

        idx = cls.idx()
        if value in idx:
            return idx[value]

        raise ValueError(
            f"Invalid label: {value} for {cls.__name__}."
            + f" Valid labels: {list(idx.keys())}"
        )
