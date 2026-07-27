import unittest

from ds import LankaData, VisualFactory
from ds.thing.concept.person.Religion import Religion
from ds.visual.PieChart import PieChart


class TestCase(unittest.TestCase):

    @staticmethod
    def _get_scenarios():
        return [
            (
                "Person/Time*Province=LK-1*Religion=hindu/Count",
                "BarChart",
                ("Time", "Count"),
            ),
            (
                "Person/Time=2012*Province=LK-2*Religion/Count",
                "PieChart",
                ("Religion", "Count"),
            ),
            (
                "Person/Time=2012*Province*Religion/Count",
                "StackedBarChart",
                ("Province", "Religion", "Count"),
            ),
            (
                "Person/Time=2012*Province*Religion=buddhist/Count",
                "MapVisual",
                ("Province", "Count"),
            ),
        ]

    def test_method(self):
        visual_class_idx = {
            visual_class.__name__: visual_class
            for visual_class in VisualFactory.visual_class_list()
        }
        for query_str, visual_class_name, params in self._get_scenarios():
            datumset = LankaData[query_str]
            visual_class = visual_class_idx[visual_class_name]
            with self.subTest(
                query_str=query_str,
                visual_class=visual_class_name,
            ):
                visual = visual_class(datumset, *params)
                visual.draw()
                self.assertTrue(visual.image_file.exists())

    def test_concept_color_map(self):
        query_str = "Person/Time=2012*Province=LK-2*Religion/Count"
        datumset = LankaData[query_str]
        visual = PieChart(datumset, "Religion", "Count")
        expected_color_map = Religion.get_color_map()
        n_matches = 0
        for value, color in visual.x_color_idx.items():
            if value in expected_color_map:
                self.assertEqual(color, expected_color_map[value])
                n_matches += 1
        self.assertGreater(n_matches, 0)
