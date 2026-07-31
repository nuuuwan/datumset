import unittest

from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.query.Query import Query
from ds.thing.concept.atom.Int import Int
from ds.visual.VisualFactory import VisualFactory


class TestCase(unittest.TestCase):

    def _build_mekko(self, data, dim_keys="X+Y"):
        query = Query(f"Entity/{dim_keys}/Count/MekkoChart")
        n_dim_keys = dim_keys.split("+")
        datums = []
        for row in data:
            dim_values = row[:-1]
            value = row[-1]
            dim_idx = {
                key: Int(val) for key, val in zip(n_dim_keys, dim_values)
            }
            datums.append(
                Datum(
                    query,
                    dim_idx,
                    {"Count": Int(value)},
                )
            )
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

    def test_small_x_labels_aggregated_into_other(self):
        data = [
            ("w1", "y1", "tiny_a", 1),
            ("w1", "y2", "tiny_a", 1),
            ("w1", "y1", "small_b", 2),
            ("w1", "y2", "small_b", 2),
            ("w1", "y1", "large_c", 200),
            ("w1", "y2", "large_c", 200),
            ("w1", "y1", "large_d", 1),
            ("w1", "y2", "large_d", 1),
            ("w1", "y1", "big_e", 1),
            ("w1", "y2", "big_e", 1),
            ("w1", "y1", "big_f", 1),
            ("w1", "y2", "big_f", 1),
            ("w1", "y1", "big_g", 1),
            ("w1", "y2", "big_g", 1),
            ("w1", "y1", "big_h", 1),
            ("w1", "y2", "big_h", 1),
        ]
        mekko = self._build_mekko(data, dim_keys="W+Y+X")
        self.assertEqual(mekko.x_dim_key, "X")
        x_labels, stack_labels, data = mekko._get_mekko_data(
            mekko.display_datumsets[0]
        )
        self.assertIn("_other_X", x_labels)
        self.assertNotIn("tiny_a", x_labels)
        self.assertNotIn("small_b", x_labels)
        self.assertIn("large_c", x_labels)
        other_total = sum(data[s]["_other_X"] for s in stack_labels)
        self.assertEqual(other_total, 16)

    def test_other_category_label_is_suffixed(self):
        data = [
            ("w1", "y1", "tiny_a", 1),
            ("w1", "y2", "tiny_a", 1),
            ("w1", "y1", "a2", 1),
            ("w1", "y2", "a2", 1),
            ("w1", "y1", "a3", 1),
            ("w1", "y2", "a3", 1),
            ("w1", "y1", "a4", 1),
            ("w1", "y2", "a4", 1),
            ("w1", "y1", "a5", 1),
            ("w1", "y2", "a5", 1),
            ("w1", "y1", "large_b", 95),
        ]
        mekko = self._build_mekko(data, dim_keys="W+Y+X")
        self.assertEqual(mekko.x_dim_key, "X")
        label = mekko._format_mekko_x_label("_other_X")
        self.assertEqual(label, "Other X")
