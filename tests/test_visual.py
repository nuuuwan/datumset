import colorsys
import unittest

import matplotlib.colors as mcolors

from ds import LankaData, VisualFactory
from ds.thing.concept.person.Religion import Religion
from ds.visual.MapVisual import MapVisual
from ds.visual.marimekko.MarimekkoChart import MarimekkoChart
from ds.visual.PieChart import PieChart
from ds.visual.StackedBarChart import StackedBarChart


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
