import colorsys
import unittest

import matplotlib.colors as mcolors

from ds import LankaData, VisualFactory
from ds.thing.concept.person.Religion import Religion
from ds.visual.MapVisual import MapVisual
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
                "Person/Time=2012*Province*Religion/Count",
                "PieChart",
            ),
            (
                "Person/Time=2012*Province*Religion/Count",
                "StackedBarChart",
            ),
            (
                "Person/Time=2012*District*Religion/Count",
                "StackedBarChart",
            ),
            (
                "Person/Time=2012*Province*Religion=buddhist/Count",
                "MapVisual",
            ),
            (
                "Person/Time=2012*District<Province=western*Religion/Count",
                "StackedBarChart",
            ),
            (
                "Person/Time=2012*PD<District=colombo*Religion=islam/Count",
                "MapVisual",
            ),
            (
                "Person/Time=2012*DSD<District=gampaha*Religion/Count",
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

    def test_concept_color_map(self):
        query_str = "Person/Time=2012*Province=Central*Religion/Count"
        datumset = LankaData[query_str]
        visual = PieChart(datumset)
        expected_color_map = Religion.get_color_map()
        n_matches = 0
        for value, color in visual.x_color_idx.items():
            if value in expected_color_map:
                self.assertEqual(color, expected_color_map[value])
                n_matches += 1
        self.assertGreater(n_matches, 0)

    def test_map_concept_color_map_hsl(self):
        query_str = "Person/Time=2012*Province*Religion=buddhist/Count"
        datumset = LankaData[query_str]
        visual = MapVisual(datumset)
        cmap = visual._get_value_cmap()
        base_color = Religion.get_color_map()["buddhist"]
        base_h, base_l, base_s = colorsys.rgb_to_hls(
            *mcolors.to_rgb(base_color)
        )
        low_h, low_l, low_s = colorsys.rgb_to_hls(*cmap(0.0)[:3])
        high_h, high_l, high_s = colorsys.rgb_to_hls(*cmap(1.0)[:3])
        self.assertAlmostEqual(base_h, low_h, places=3)
        self.assertAlmostEqual(base_h, high_h, places=3)
        self.assertAlmostEqual(base_s, low_s, places=3)
        self.assertAlmostEqual(base_s, high_s, places=3)
        self.assertGreater(low_l, high_l)
        self.assertGreater(base_l, high_l)

    def test_visual_title_case_category_values(self):
        query_str = (
            "Person/Time*Province=Western*Religion=roman_catholic/Count"
        )
        datumset = LankaData[query_str]
        visual = PieChart(datumset)
        subfigure_title = visual._get_subfigure_title(
            visual.display_datumsets[0],
            visual._excluded_dim_keys(),
        )
        self.assertIn("Roman Catholic", subfigure_title)
        self.assertNotIn("roman_catholic", subfigure_title)
        self.assertEqual("Buddhist", visual._format_visual_value("buddhist"))
        self.assertEqual("Hindu", visual._format_visual_value("hindu"))
        self.assertEqual("Western", visual._format_visual_value("Western"))

    def test_pie_percentage_only_labels(self):
        query_str = "Person/Time=2012*Province=Western*Religion/Count"
        datumset = LankaData[query_str]
        visual = PieChart(datumset)
        autopct = visual._build_autopct()
        self.assertEqual("10%", autopct(10.0))
        self.assertEqual("<0.5%", autopct(0.4))

    def test_pie_radius_scaling(self):
        query_str = "Person/Time=2012*Province=Western*Religion/Count"
        datumset = LankaData[query_str]
        visual = PieChart(datumset)
        self.assertEqual(1.0, visual._get_pie_radius(50.0, 100.0, 1))
        self.assertAlmostEqual(0.5, visual._get_pie_radius(25.0, 100.0, 4))

    def test_contrast_text_color(self):
        query_str = "Person/Time=2012*Province=Western*Religion/Count"
        datumset = LankaData[query_str]
        visual = PieChart(datumset)
        self.assertEqual(
            visual.CONTRAST_LIGHT_TEXT_COLOR,
            visual._get_contrast_text_color("#111111"),
        )
        self.assertEqual(
            visual.CONTRAST_DARK_TEXT_COLOR,
            visual._get_contrast_text_color("#f3f3f3"),
        )

    def test_child_region_query_format_in_image_path(self):
        query_str = "Person/Time=2012*District<Province=western*Religion/Count"
        datumset = LankaData[query_str]
        visual = StackedBarChart(
            datumset,
        )
        self.assertIn("District<Province=western", visual.image_file.path)

    def test_map_visual_shows_only_regions_with_data(self):
        query_str = (
            "Person/Time=2012*DSD<District=colombo*Religion=islam/Count"
        )
        datumset = LankaData[query_str]
        visual = MapVisual(datumset)
        sub_datumset = visual.display_datumsets[0]
        gdf = visual._get_gdf_with_values(sub_datumset)
        self.assertGreater(len(gdf), 0)
        self.assertFalse(gdf["value"].isna().any())
        self.assertEqual(
            len(gdf),
            len(visual._get_region_values_for(sub_datumset)),
        )
