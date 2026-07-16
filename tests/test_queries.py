import unittest

from ds import LankaData, MatchedDatumset


class TestCase(unittest.TestCase):
    def test_basic(self):
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

            mds2 = MatchedDatumset.from_str(mds1.to_str())
            mds3 = MatchedDatumset.from_str(mds2.to_str())

            self.assertEqual(mds1, mds2)
            self.assertEqual(mds1, mds3)
