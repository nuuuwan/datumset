import unittest

from ds import Datumset, LankaData


class TestCase(unittest.TestCase):
    def test_valid(self):
        for query_str in [
            "Person/Time*District*Religion/Count",
            "Person/Time*Province*Religion/Count",
            "Person/Time*ED*Religion/Count",
            "Person/Time*PD*Religion/Count",
        ]:
            ds1 = LankaData[query_str]
            ds2 = Datumset.from_str(ds1.to_str())
            self.assertEqual(ds1, ds2)

            ds3 = Datumset.from_str(ds2.to_str())
            self.assertEqual(ds1, ds3)

    def test_invalid(self):
        for query_str in [
            "Person/Time*GND*Religion/Count",
            "Person/Time*DSD*Ethnicity1/Count",
        ]:
            with self.assertRaises(ValueError):
                LankaData[query_str]
