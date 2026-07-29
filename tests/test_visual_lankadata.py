import unittest

from ds import VisualLankaData


class TestCase(unittest.TestCase):

    @staticmethod
    def _get_scenarios():
        return [
            # BarChart
            "Person/Time*Province*Religion/Count/BarChart",
            "Person/Time*Province=Western*Religion/Count/BarChart",
            "Person/Time*Province=Western*Religion=hindu/Count/BarChart",
            # PieChart
            "Person/Time=2024*Province*Religion/Count/PieChart",
            "Person/Time=2024*Province=northern*Religion/Count/PieChart",
            # StackedBarChart
            "Person/Time=2024*Province*Religion/Count/StackedBarChart",
            "Person/Time=2024*District*Religion/Count/StackedBarChart",
            "Person/Time=2024*District<Province=western*Religion/Count"
            + "/StackedBarChart",
            "Person/Time=2024*DSD<District=gampaha*Religion/Count"
            + "/StackedBarChart",
            "Vote/ElectionType=presidential*Time=2024*Province*Party/Count"
            + "/StackedBarChart",
            # MarimekkoChart
            "Vote/ElectionType=presidential*Time=2024*Province*Party/Count"
            + "/MarimekkoChart",
            "Vote/ElectionType=presidential*Time=2019*Province*Party/Count"
            + "/MarimekkoChart",
            # MapVisual
            "Person/Time=2024*Province*Religion/Count/MapVisual",
            "Person/Time=2024*Province*Religion=buddhist/Count/MapVisual",
            "Person/Time=2024*PD<District=colombo*Religion=islam/Count"
            + "/MapVisual",
        ]

    def test_basic(self):
        for visual_query_str in self._get_scenarios():
            image_file = VisualLankaData[visual_query_str]
            self.assertTrue(image_file.exists())
