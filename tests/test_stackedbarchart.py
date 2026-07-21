import os
import unittest

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.ThingFactory import ThingFactory
from ds.visual.StackedBarChart import StackedBarChart


def _make_datum(district, religion, count):
    return Datum(
        entity_class=ThingFactory["Person"],
        dim_idx=dict(
            District=ThingFactory["District"][district],
            Religion=ThingFactory["Religion"][religion],
            Time=ThingFactory["Time"]("2012"),
        ),
        cell_idx=dict(Count=ThingFactory["Int"](count)),
    )


def _make_datumset():
    return Datumset(
        _make_datum("LK-11", "Buddhist", 100),
        _make_datum("LK-11", "Hindu", 50),
        _make_datum("LK-12", "Buddhist", 200),
        _make_datum("LK-12", "Hindu", 80),
    )


class TestStackedBarChart(unittest.TestCase):

    def setUp(self):
        self.datumset = _make_datumset()
        self.chart = StackedBarChart(
            self.datumset, 'District', 'Religion', 'Count'
        )

    def test_init(self):
        self.assertIs(self.chart.datumset, self.datumset)
        self.assertEqual(self.chart.x_dim_key, 'District')
        self.assertEqual(self.chart.stack_dim_key, 'Religion')
        self.assertEqual(self.chart.y_cell_key, 'Count')

    def test_get_data(self):
        x_labels, stack_labels, data = self.chart._get_data()
        self.assertEqual(x_labels, ['LK-11', 'LK-12'])
        self.assertEqual(len(stack_labels), 2)
        for s in stack_labels:
            self.assertIn('LK-11', data[s])
            self.assertIn('LK-12', data[s])

    def test_excluded_dim_keys(self):
        excluded = self.chart._excluded_dim_keys()
        self.assertIn('District', excluded)
        self.assertIn('Religion', excluded)

    def test_build_title(self):
        title = self.chart._build_title()
        self.assertIn('Count', title)
        self.assertIn('District', title)
        self.assertIn('Religion', title)

    def test_build_subtitle(self):
        subtitle = self.chart._build_subtitle()
        self.assertIn('Person', subtitle)
        self.assertIn('Time', subtitle)

    def test_image_path(self):
        path = self.chart._image_path()
        self.assertTrue(path.startswith('image' + os.sep))
        self.assertTrue(path.endswith('.png'))

    def test_draw_saves_image(self):
        self.chart.draw()
        self.assertTrue(os.path.exists(self.chart._image_path()))

    def test_draw_returns_fig(self):
        import matplotlib.figure

        fig = self.chart.draw()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == '__main__':
    unittest.main()
