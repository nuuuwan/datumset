import unittest

from ds import LankaData, MatchedDatumset


class TestCase(unittest.TestCase):
    def test_valid(self):
        for query_str in [
            "Person/2012/Religion*District",
            "Person/2024/Religion*District",
            "Person/2024/District*Religion",
            "Person/2024/District",
            "Person/2024/Religion",
            "Person/2012+2024/Religion",
            "Person+House/2012+2024/Religion",
            "House+Person/2012+2024/Religion",
        ]:
            mds1 = LankaData[query_str]
            print("=" * 80)
            print(mds1)

            mds2 = MatchedDatumset.from_str(mds1.to_str())
            print("-" * 80)
            print(mds2)
            self.assertEqual(mds1, mds2)

            # mds3 = MatchedDatumset.from_str(mds2.to_str())
            # self.assertEqual(mds1, mds3)

    def test_invalid(self):
        for query_str in [
            "Person/2024/Religion*Invalid",
            "Person/3999/Religion*Invalid",
            "Cat/2024/Religion*Invalid",
        ]:
            with self.assertRaises(ValueError):
                output = LankaData[query_str]
                self.assertIsNone(output)
