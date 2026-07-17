import time
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
            ds2 = Datumset.from_data(ds1.to_data())
            self.assertEqual(ds1, ds2)

    def test_performance(self):
        for query_str in [
            "Person/Time*District*Religion/Count",
            "Person/Time*Province*Religion/Count",
            "Person/Time*ED*Religion/Count",
            "Person/Time*PD*Religion/Count",
        ]:
            t0 = time.time()
            datumset = LankaData[query_str]
            self.assertIsNotNone(datumset)
            elapsed_ms = (time.time() - t0) * 1000.0
            MAX_T_MS = 100.0
            self.assertLess(
                elapsed_ms,
                MAX_T_MS,
                f"{query_str} took {elapsed_ms:.2f}ms > {MAX_T_MS}ms",
            )

    def test_invalid(self):
        for query_str in [
            "Person/Time*GND*Religion1/Count",
            "Person/Time*DSD*Ethnicity1/Count",
        ]:
            with self.assertRaises(ValueError):
                LankaData[query_str]
