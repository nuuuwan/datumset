import unittest

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.query.Query import Query
from ds.thing.concept.atom.Int import Int
from ds.visual.VisualFactory import VisualFactory


class TestCase(unittest.TestCase):

    def _build_mekko(self, data):
        query = Query("Entity/X+Y/Count/MekkoChart")
        datums = [
            Datum(
                query,
                {"X": Int(x), "Y": Int(y)},
                {"Count": Int(value)},
            )
            for x, y, value in data
        ]
        datumset = Datumset(*datums)
        MekkoChart = VisualFactory["MekkoChart"]
        return MekkoChart(datumset)

    def test_x_order_by_dominant_stack_share(self):
        data = [
            ("a", "alpha", 90),
            ("a", "beta", 10),
            ("b", "alpha", 50),
            ("b", "beta", 50),
            ("c", "alpha", 30),
            ("c", "beta", 70),
        ]
        mekko = self._build_mekko(data)
        x_labels, _, _ = mekko._get_data(mekko.display_datumsets[0])
        self.assertEqual(x_labels, ["alpha", "beta"])

    def test_x_order_with_tied_shares(self):
        data = [
            ("a", "alpha", 50),
            ("a", "beta", 50),
            ("b", "alpha", 50),
            ("b", "beta", 50),
        ]
        mekko = self._build_mekko(data)
        x_labels, _, _ = mekko._get_data(mekko.display_datumsets[0])
        self.assertEqual(len(x_labels), 2)
