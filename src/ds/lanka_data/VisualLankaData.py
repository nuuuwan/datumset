import json
from functools import cache

from utils_future import Log

from ds.lanka_data.LankaData import LankaData
from ds.visual.VisualFactory import VisualFactory

log = Log("VisualLankaData")


class VisualLankaData:
    @classmethod
    @cache
    def __class_getitem__(cls, visual_query_str):
        tokens = visual_query_str.rsplit("/")
        if len(tokens) < 3:
            raise ValueError(
                f"Invalid visual_query_str: {visual_query_str}"
                + " (must have at least 3 tokens)"
            )

        query_str = "/".join(tokens[:3])
        datumset = LankaData[query_str]

        if len(tokens) == 4:
            visual_class_name = tokens[3]
            visual_class = VisualFactory[visual_class_name]
            visual = visual_class(datumset)
            visual.draw()
            return visual.image_file

        print(json.dumps(datumset.to_data(), indent=4))
