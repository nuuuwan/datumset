import unittest

from ds.datum.Datum import Datum
from ds.query.Query import Query
from ds.thing.ThingFactory import ThingFactory


class TestCase(unittest.TestCase):

    def _build_datum(self):
        return Datum(
            entity_class=ThingFactory["Person"],
            dim_idx=dict(
                Time=ThingFactory["Time"]("2012"),
                District=ThingFactory["District"]["colombo"],
                Religion=ThingFactory["Religion"]["Buddhist"],
            ),
            cell_idx=dict(
                Count1=ThingFactory["Int"](123),
                Count2=ThingFactory["Int"](112),
            ),
        )

    def test_serialize(self):
        datum = self._build_datum()

        data = datum.to_data()
        self.assertEqual(
            data,
            {
                "Person": {
                    "Time:2012": {
                        "District:colombo": {
                            "Religion:buddhist": {
                                "Count1": "Int:123",
                                "Count2": "Int:112",
                            }
                        }
                    }
                }
            },
        )

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
