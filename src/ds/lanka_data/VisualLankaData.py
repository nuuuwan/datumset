from functools import cache

from utils_future import Log

from ds.lanka_data.LankaData import LankaData
from ds.visual.VisualFactory import VisualFactory

log = Log("VisualLankaData")


class VisualLankaData:
    @classmethod
    @cache
    def __class_getitem__(cls, visual_query_str):
        query_str, visual_class_name = visual_query_str.rsplit("/", 1)
        datumset = LankaData[query_str]
        if len(datumset) == 0:
            raise ValueError(f"No data found for query: {query_str}")
        visual_class = VisualFactory[visual_class_name]
        visual = visual_class(datumset)
        visual.draw()
        return visual.image_file
