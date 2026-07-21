import os
import unittest

import matplotlib.figure

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.ThingFactory import ThingFactory
from ds.visual.MapVisual import MapVisual

_DISTRICTS = [
    ('LK-11', 200),
    ('LK-12', 180),
    ('LK-13', 160),
    ('LK-21', 140),
    ('LK-22', 120),
    ('LK-23', 100),
    ('LK-31', 90),
    ('LK-32', 80),
    ('LK-33', 70),
]


def _make_datum(district_id, count):
    return Datum(
        entity_class=ThingFactory['Person'],
        dim_idx=dict(
            District=ThingFactory['District'][district_id],
            Time=ThingFactory['Time']('2012'),
        ),
        cell_idx=dict(Count=ThingFactory['Int'](count)),
    )


def _make_datumset():
    return Datumset(*[_make_datum(d, v) for d, v in _DISTRICTS])


class TestMapVisual(unittest.TestCase):

    def setUp(self):
        self.chart = MapVisual(_make_datumset(), 'District', 'Count')

    def test_init(self):
        self.assertEqual(self.chart.region_dim_key, 'District')
        self.assertEqual(self.chart.y_cell_key, 'Count')

    def test_get_region_values(self):
        rv = self.chart._get_region_values()
        self.assertEqual(rv['LK-11'], 200.0)
        self.assertEqual(len(rv), len(_DISTRICTS))

    def test_excluded_dim_keys(self):
        self.assertIn('District', self.chart._excluded_dim_keys())

    def test_build_title(self):
        self.assertEqual(self.chart._build_title(), 'Count by District')

    def test_image_path(self):
        path = self.chart._image_path()
        self.assertTrue(path.startswith('image' + os.sep))
        self.assertTrue(path.endswith('.png'))

    def test_draw_returns_fig(self):
        fig = self.chart.draw()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == '__main__':
    unittest.main()
