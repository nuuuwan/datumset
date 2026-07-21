import unittest

import matplotlib.figure

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.ThingFactory import ThingFactory
from ds.visual.BarChart import BarChart


def _make_datum(year, count):
    return Datum(
        entity_class=ThingFactory["Person"],
        dim_idx=dict(
            District=ThingFactory["District"]["LK-11"],
            Time=ThingFactory["Time"](year),
        ),
        cell_idx=dict(Count=ThingFactory["Int"](count)),
    )


def _make_datumset():
    return Datumset(
        _make_datum("2012", 100),
        _make_datum("2013", 150),
        _make_datum("2014", 120),
    )


class TestBarChartByTime(unittest.TestCase):

    def setUp(self):
        self.chart = BarChart(_make_datumset(), "Time", "Count")

    def test_get_xy(self):
        x_labels, y_values = self.chart._get_xy()
        self.assertEqual(x_labels, ["2012", "2013", "2014"])
        self.assertEqual(y_values, [100.0, 150.0, 120.0])

    def test_title(self):
        self.assertEqual(self.chart._build_title(), "Count by Time")

    def test_subtitle_has_district(self):
        subtitle = self.chart._build_subtitle()
        self.assertIn("District", subtitle)
        self.assertIn("LK-11", subtitle)

    def test_draw(self):
        fig = self.chart.draw()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == "__main__":
    unittest.main()
