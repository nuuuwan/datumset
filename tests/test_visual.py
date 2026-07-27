import unittest

from ds import LankaData, VisualFactory


class TestCase(unittest.TestCase):
    def test_method(self):
        datumset = LankaData["Person/Time*Province*Religion/Count"]
        visual_params_idx = {
            "BarChart": ("Religion", "Count"),
            "MapVisual": ("Province", "Count"),
            "PieChart": ("Religion", "Count"),
            "StackedBarChart": ("Province", "Religion", "Count"),
        }
        for visual_class in VisualFactory.visual_class_list():
            with self.subTest(visual_class=visual_class.__name__):
                params = visual_params_idx[visual_class.__name__]
                visual = visual_class(datumset, *params)
                visual.draw()
                self.assertTrue(visual.image_file.exists())
