import unittest

from ds import LankaData, VisualFactory


class TestCase(unittest.TestCase):

    @staticmethod
    def _get_scenarios():
        return [
            (
                "Person/Time*Province=Western*Religion=hindu/Count",
                "BarChart",
            ),
            (
                "Person/Time=2024*Province*Religion/Count",
                "PieChart",
            ),
            (
                "Person/Time=2024*Province*Religion/Count",
                "StackedBarChart",
            ),
            (
                "Person/Time=2024*District*Religion/Count",
                "StackedBarChart",
            ),
            (
                "Person/Time=2024*Province*Religion=buddhist/Count",
                "MapVisual",
            ),
            (
                "Person/Time=2024*District<Province=western*Religion/Count",
                "StackedBarChart",
            ),
            (
                "Person/Time=2024*PD<District=colombo*Religion=islam/Count",
                "MapVisual",
            ),
            (
                "Person/Time=2024*DSD<District=gampaha*Religion/Count",
                "StackedBarChart",
            ),
            (
                "Vote/ElectionType=Presidential*Time=2024*Province*Party/Count",
                "StackedBarChart",
            ),
            (
                "Vote/ElectionType=Presidential*Time=2024*Province*Party/Count",
                "MarimekkoChart",
            ),
        ]

    def test_basic(self):
        visual_class_idx = {
            visual_class.__name__: visual_class
            for visual_class in VisualFactory.visual_class_list()
        }
        for query_str, visual_class_name in self._get_scenarios():
            datumset = LankaData[query_str]
            visual_class = visual_class_idx[visual_class_name]
            with self.subTest(
                query_str=query_str,
                visual_class=visual_class_name,
            ):
                visual = visual_class(datumset)
                visual.draw()
                self.assertTrue(visual.image_file.exists())
