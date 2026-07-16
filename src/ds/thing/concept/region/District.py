from functools import cache

from ds.thing.concept.region.Region import Region
from utils_future import WWW, Directory, File, JSONFile


class District(Region):

    @classmethod
    def region_class_id(cls):
        return cls.__name__.lower()

    @classmethod
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
