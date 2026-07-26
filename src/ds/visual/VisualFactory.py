from ds.visual.BarChart import BarChart
from ds.visual.MapVisual import MapVisual
from ds.visual.PieChart import PieChart
from ds.visual.StackedBarChart import StackedBarChart


class VisualFactory:

    @classmethod
    def visual_class_list(cls):
        return [
            BarChart,
            MapVisual,
            PieChart,
            StackedBarChart,
        ]

    @classmethod
    def __class_getitem__(cls, visual_class_name):
        for visual_class in cls.visual_class_list():
            if visual_class.__name__ == visual_class_name:
                return visual_class
        raise ValueError(f"Visual class '{visual_class_name}' not found")
