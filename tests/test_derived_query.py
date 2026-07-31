import unittest

from ds.lanka_data.LankaData import LankaData

BASE_QUERY = "Person/Time+Province+Religion/Count"
GROUP_DIMS = ["Time", "Province"]
TARGET_DIM = "Religion"


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
        top_datumset = LankaData["Person/Time+Province+Religion/Top"]
        base_datumset = LankaData[BASE_QUERY]

        expected = self._get_expected_top(
            base_datumset, GROUP_DIMS, TARGET_DIM
        )

        self.assertGreater(len(top_datumset), 0)
        self.assertEqual(len(top_datumset), len(expected))
        for datum in top_datumset:
            key = tuple(datum.dim_idx[dim].get_value() for dim in GROUP_DIMS)
            self.assertEqual(
                datum.dim_idx[TARGET_DIM].get_value(),
                expected[key][1],
            )

    def test_top_reordered_dims(self):
        top_datumset = LankaData["Person/Religion+Time+Province/Top"]
        base_datumset = LankaData[BASE_QUERY]

        expected = self._get_expected_top(
            base_datumset, GROUP_DIMS, TARGET_DIM
        )

        self.assertGreater(len(top_datumset), 0)
        self.assertEqual(len(top_datumset), len(expected))
        for datum in top_datumset:
            key = tuple(datum.dim_idx[dim].get_value() for dim in GROUP_DIMS)
            self.assertEqual(
                datum.dim_idx[TARGET_DIM].get_value(),
                expected[key][1],
            )

    def test_bottom(self):
        bottom_datumset = LankaData["Person/Time+Province+Religion/Bottom"]
        base_datumset = LankaData[BASE_QUERY]

        expected = {}
        for datum in base_datumset:
            key = tuple(datum.dim_idx[dim].get_value() for dim in GROUP_DIMS)
            count = float(datum.cell_idx["Count"].get_value())
            target = datum.dim_idx[TARGET_DIM].get_value()
            if key not in expected or count < expected[key][0]:
                expected[key] = (count, target)

        self.assertGreater(len(bottom_datumset), 0)
        self.assertEqual(len(bottom_datumset), len(expected))
        for datum in bottom_datumset:
            key = tuple(datum.dim_idx[dim].get_value() for dim in GROUP_DIMS)
            self.assertEqual(
                datum.dim_idx[TARGET_DIM].get_value(),
                expected[key][1],
            )

    def test_rank(self):
        rank_datumset = LankaData["Person/Time+Province+Religion/Rank"]
        base_datumset = LankaData[BASE_QUERY]

        self.assertGreater(len(rank_datumset), 0)
        self.assertEqual(len(rank_datumset), len(base_datumset))
        for datum in rank_datumset:
            self.assertIn("Rank", datum.cell_idx)
            rank_val = int(datum.cell_idx["Rank"].get_value())
            self.assertGreaterEqual(rank_val, 1)

    def test_share(self):
        share_datumset = LankaData["Person/Time+Province+Religion/Share"]
        base_datumset = LankaData[BASE_QUERY]

        self.assertGreater(len(share_datumset), 0)
        self.assertEqual(len(share_datumset), len(base_datumset))

        group_sums = {}
        for datum in share_datumset:
            key = tuple(datum.dim_idx[dim].get_value() for dim in GROUP_DIMS)
            share = float(datum.cell_idx["Share"].get_value())
            group_sums[key] = group_sums.get(key, 0.0) + share
        for total in group_sums.values():
            self.assertAlmostEqual(total, 1.0, places=9)

    def test_change(self):
        change_datumset = LankaData["Person/Province+Religion+Time/Change"]
        base_datumset = LankaData["Person/Province+Religion+Time/Count"]

        self.assertGreater(len(change_datumset), 0)
        for datum in change_datumset:
            self.assertIn("Change", datum.cell_idx)

        groups = set()
        for datum in base_datumset:
            groups.add(
                (
                    datum.dim_idx["Province"].get_value(),
                    datum.dim_idx["Religion"].get_value(),
                )
            )
        self.assertEqual(len(change_datumset), len(groups))


if __name__ == "__main__":
    unittest.main()
