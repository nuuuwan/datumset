from dataclasses import dataclass
from functools import cache

from utils_future import WWW, Directory, File, JSONFile, Log, String

from ds.thing.concept.CategoryConcept import CategoryConcept

log = Log("Region")


@dataclass(frozen=True)
class Region(CategoryConcept):

    @classmethod
    @cache
    def region_class_id(cls):
        return cls.__name__.lower()

    @classmethod
    @cache
    def valid_values(cls):
        return [r.get_value() for r in cls.list()]

    @cache
    def get_ent(self):
        idx = self.get_ent_idx_by_value()

        if self.get_value() in idx:
            return idx[self.get_value()]

        raise ValueError(f"Could not find ent for {self}")

    @classmethod
    @cache
    def get_ents(cls):
        dir_temp = Directory.get_temp("datumset", "regions")
        dir_temp.make()
        data_file = JSONFile(
            dir_temp,
            f"{cls.region_class_id()}s.json",
        )
        url = (
            "https://raw.githubusercontent.com"
            + "/nuuuwan"
            + "/lk_admin_regions/refs/heads/main"
            + f"/data/ents/{cls.region_class_id()}s.json"
        )
        if not data_file.exists():
            log.debug(f"Downloading {cls.region_class_id()}s from {url}")
        WWW(url).download(File(data_file.path))
        data_list = data_file.read()
        return data_list

    @classmethod
    @cache
    def get_ent_idx_by_id(cls):
        return {d["id"]: d for d in cls.get_ents()}

    @classmethod
    @cache
    def get_ent_idx_by_value(cls):
        return {String(d["name"]).snake: d for d in cls.get_ents()}

    @classmethod
    @cache
    def list(cls):
        data_list = cls.get_ents()
        return [cls(String(d["name"]).snake) for d in data_list]

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

    @classmethod
    @cache
    def from_region_id(cls, region_id: str):
        idx = cls.get_ent_idx_by_id()
        if region_id in idx:
            return cls(String(idx[region_id]["name"]).snake)
        raise ValueError(
            f"Invalid region_id: {region_id} for {cls.__name__}."
            + f" Valid region_ids: {list(idx.keys())}"
        )

    @classmethod
    def can_shorten(cls):
        return True
