from ds.visual.BarChart import BarChart
from ds.visual.dorling.Dorling import Dorling
from ds.visual.hex_map.HexMap import HexMap
from ds.visual.hex_map.UnitHexMap import UnitHexMap
from ds.visual.map.Cartogram import Cartogram
from ds.visual.map.Map import Map
from ds.visual.mekko.MekkoChart import MekkoChart
from ds.visual.pie_chart.PieChart import PieChart
from ds.visual.square_map.SquareMap import SquareMap
from ds.visual.square_map.UnitSquareMap import UnitSquareMap
from ds.visual.stacked_bar_chart.StackedBarChart import StackedBarChart
from ds.visual.treemap.TreeMap import TreeMap


class VisualFactory:

    @classmethod
    def visual_class_list(cls):
        return [
            BarChart,
            Map,
            Cartogram,
            Dorling,
            HexMap,
            UnitHexMap,
            SquareMap,
            UnitSquareMap,
            MekkoChart,
            PieChart,
            StackedBarChart,
            TreeMap,
        ]

    @classmethod
    def __class_getitem__(cls, visual_class_name):
        for visual_class in cls.visual_class_list():
            if visual_class.__name__ == visual_class_name:
                return visual_class
        raise ValueError(
            f"Visual class '{visual_class_name}' not found"
        )  # pragma: no cover
