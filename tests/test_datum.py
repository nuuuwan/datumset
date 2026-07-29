import json
import os
import unittest

from ds.datum.Datum import Datum
from ds.query.Query import Query

DIR_DATA = os.path.join(os.path.dirname(__file__), "data")


class TestCase(unittest.TestCase):

    def _get_data(self):
        path = os.path.join(DIR_DATA, "test_datum.json")
        with open(path) as fin:
            return json.load(fin)

    def _build_datum(self):
        return Datum.from_data(self._get_data())

    def test_serialize(self):
        datum = self._build_datum()
        data = datum.to_data()
        self.assertEqual(data, self._get_data())
        datum2 = Datum.from_data(data)
        self.assertEqual(datum, datum2)

    def test_match_basic(self):
        datum = self._build_datum()

        self.assertTrue(datum.is_match_entity("Person"))
        self.assertFalse(datum.is_match_entity("House"))

        self.assertTrue(datum.is_match_dim_idx("Time*District*Religion"))
        self.assertFalse(datum.is_match_dim_idx("Time*District"))
        self.assertTrue(
            datum.is_match_dim_idx("Time=2012*District*Religion=buddhist")
        )
        self.assertFalse(
            datum.is_match_dim_idx("Time=2024*District*Religion=buddhist")
        )

        self.assertTrue(datum.is_match_cell_idx("Count1*Count2"))
        self.assertFalse(datum.is_match_cell_idx("Count1"))

        self.assertTrue(
            datum.is_match(
                Query("Person/Time*District*Religion/Count1*Count2")
            )
        )
        self.assertFalse(
            datum.is_match(Query("Person/Time*District*Religion/Count1"))
        )

    def test_match_dim_values(self):
        datum = self._build_datum()

        self.assertTrue(
            datum.is_match_dim_idx("Time=2012*District*Religion=buddhist")
        )
        self.assertFalse(
            datum.is_match_dim_idx("Time=2024*District*Religion=buddhist")
        )
        self.assertTrue(
            datum.is_match(
                Query(
                    "Person/Time=2012*District*Religion=buddhist/Count1*Count2"
                )
            )
        )
        self.assertFalse(
            datum.is_match(
                Query(
                    "Person/Time=2024*District*Religion=buddhist/Count1*Count2"
                )
            )
        )

    def test_match_child_region_dim_spec(self):
        datum = self._build_datum()

        self.assertTrue(
            datum.is_match_dim_idx(
                "Time=2012*District<Province=western*Religion=buddhist"
            )
        )
        self.assertFalse(
            datum.is_match_dim_idx(
                "Time=2012*District<Province=southern*Religion=buddhist"
            )
        )
