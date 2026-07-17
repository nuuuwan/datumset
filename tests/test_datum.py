import unittest

from ds.datum.Datum import Datum
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
