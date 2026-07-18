import unittest

from ds.adapters.RegionValueAdapter import RegionValueAdapter
from ds.thing.concept.person.Religion import Religion
from ds.thing.entity.Person import Person


class TestCase(unittest.TestCase):
    def test_basic(self):
        d_list = [
            dict(
                region_id="LK-11",
                region_name="Colombo",
                region_ent_type="district",
                values=dict(
                    buddhist=1,
                    hindu=2,
                    islam=3,
                    roman_catholic=4,
                    other_christian=5,
                    other=1,
                ),
            )
        ]
        datumset = RegionValueAdapter.build_datumset(
            d_list,
            entity_cls=Person,
            time_str=2024,
            region_id_field="region_id",
            measurement_cls=Religion,
        )
        self.assertEqual(
            datumset.to_data(),
            {
                "Person": {
                    "Time:2024": {
                        "District:LK-11": {
                            "Religion:Buddhist": {"Count": 1},
                            "Religion:Hindu": {"Count": 2},
                            "Religion:Islam": {"Count": 3},
                            "Religion:RomanCatholic": {"Count": 4},
                            "Religion:OtherChristian": {"Count": 5},
                            "Religion:Other": {"Count": 1},
                        }
                    }
                }
            },
        )
