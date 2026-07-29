import unittest

from ds.lanka_data.LankaData import LankaData
from ds.query.DerivedQuery import DerivedQuery


class TestCase(unittest.TestCase):

    @staticmethod
    def _get_expected_top(base_datumset, group_dims, target_dim):
        expected = {}
        for datum in base_datumset:
            key = tuple(datum.dim_idx[dim].get_value() for dim in group_dims)
            count = float(datum.cell_idx["Count"].get_value())
            target = datum.dim_idx[target_dim].get_value()
            if key not in expected or count > expected[key][0]:
                expected[key] = (count, target)
        return expected

    def test_top(self):
        top_datumset = DerivedQuery["Person/Time*Province*Religion/Top"]
        base_datumset = LankaData["Person/Time*Province*Religion/Count"]

        group_dims = ["Time", "Province"]
        expected = self._get_expected_top(
            base_datumset, group_dims, "Religion"
        )

        self.assertGreater(len(top_datumset), 0)
        self.assertEqual(len(top_datumset), len(expected))
        for datum in top_datumset:
            key = tuple(datum.dim_idx[dim].get_value() for dim in group_dims)
            self.assertEqual(
                datum.dim_idx["Religion"].get_value(),
                expected[key][1],
            )


if __name__ == "__main__":
    unittest.main()
