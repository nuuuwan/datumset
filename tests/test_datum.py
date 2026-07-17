import unittest

from ds.datum.Datum import Datum
from ds.query.Query import Query
from ds.thing.ThingFactory import ThingFactory


class TestCase(unittest.TestCase):
    def test_serialize(self):
        datum = Datum(
            entity_class=ThingFactory["Person"],
            dim_idx=dict(
                Time=ThingFactory["Time"]("2012"),
                District=ThingFactory["District"]["LK-11"],
                Religion=ThingFactory["Religion"]["Buddhist"],
            ),
            cell_idx=dict(
                Count1=ThingFactory["Int"](123),
                Count2=ThingFactory["Int"](112),
            ),
        )

        data = datum.to_data()
        self.assertEqual(
            data,
            {
                "Person": {
                    "Time:2012": {
                        "District:LK-11": {
                            "Religion:Buddhist": {
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

    def test_match(self):
        datum = Datum(
            entity_class=ThingFactory["Person"],
            dim_idx=dict(
                Time=ThingFactory["Time"]("2012"),
                District=ThingFactory["District"]["LK-11"],
                Religion=ThingFactory["Religion"]["Buddhist"],
            ),
            cell_idx=dict(
                Count1=ThingFactory["Int"](123),
                Count2=ThingFactory["Int"](112),
            ),
        )

        self.assertTrue(datum.is_match_entity("Person"))
        self.assertFalse(datum.is_match_entity("House"))

        self.assertTrue(datum.is_match_dim_idx("Time*District*Religion"))
        self.assertFalse(datum.is_match_dim_idx("Time*District"))

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
