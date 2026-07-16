import unittest

from ds import Datumset, LankaData


class TestCase(unittest.TestCase):
    def test_valid(self):
        for query_str in [
            "Person/2012/District*Religion*Count",
        ]:
            ds1 = LankaData[query_str]
            ds2 = Datumset.from_str(ds1.to_str())
            self.assertEqual(ds1, ds2)

            ds3 = Datumset.from_str(ds2.to_str())
            self.assertEqual(ds1, ds3)

    # def test_invalid(self):
    #     for query_str in [
    #         "House+Person/2012+2024/Religion*Count",
    #         "Person/2024/Religion*Invalid",
    #         "Person/3999/Religion*Invalid",
    #         "Cat/2024/Religion*Invalid",
    #     ]:
    #         with self.assertRaises(ValueError):
    #             output = LankaData[query_str]
    #             self.assertIsNone(output)
