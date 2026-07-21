import os
import unittest

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.ThingFactory import ThingFactory
from ds.visual.BarChart import BarChart


def _make_datumset():
    return Datumset(
        Datum(
            entity_class=ThingFactory["Person"],
            dim_idx=dict(
                District=ThingFactory["District"]["LK-11"],
                Time=ThingFactory["Time"]("2012"),
            ),
            cell_idx=dict(Count=ThingFactory["Int"](100)),
        ),
        Datum(
            entity_class=ThingFactory["Person"],
            dim_idx=dict(
                District=ThingFactory["District"]["LK-12"],
                Time=ThingFactory["Time"]("2012"),
            ),
            cell_idx=dict(Count=ThingFactory["Int"](200)),
        ),
    )


class TestBarChart(unittest.TestCase):

    def setUp(self):
        self.datumset = _make_datumset()
        self.chart = BarChart(self.datumset, "District", "Count")

    def test_init(self):
        self.assertIs(self.chart.datumset, self.datumset)
        self.assertEqual(self.chart.x_dim_key, "District")
        self.assertEqual(self.chart.y_cell_key, "Count")

    def test_get_xy(self):
        x_labels, y_values = self.chart._get_xy()
        self.assertEqual(x_labels, ["LK-11", "LK-12"])
        self.assertEqual(y_values, [100.0, 200.0])

    def test_image_path(self):
        path = self.chart._image_path()
        self.assertTrue(path.startswith("image" + os.sep))
        self.assertIn("District", path)
        self.assertIn("Count", path)
        self.assertTrue(path.endswith(".png"))

    def test_draw_saves_image(self):
        self.chart.draw()
        self.assertTrue(os.path.exists(self.chart._image_path()))

    def test_build_title(self):
        self.assertEqual(self.chart._build_title(), "Count by District")

    def test_build_subtitle(self):
        subtitle = self.chart._build_subtitle()
        self.assertIn("Person", subtitle)
        self.assertIn("Time", subtitle)
        self.assertIn("2012", subtitle)

    def test_draw_figsize_dpi(self):
        import matplotlib.figure

        from ds.visual.Visual import Visual

        fig = self.chart.draw()
        self.assertIsInstance(fig, matplotlib.figure.Figure)
        self.assertEqual(fig.get_size_inches().tolist(), list(Visual.FIGSIZE))
        self.assertEqual(fig.dpi, Visual.DPI)

    def test_draw_returns_fig(self):
        import matplotlib.figure

        fig = self.chart.draw()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == "__main__":
    unittest.main()
