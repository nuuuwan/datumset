import unittest

from ds.db.Census2012 import Census2012


class TestCase(unittest.TestCase):
    def test_basic(self):
        datumsets = Census2012.list()
        datumset = datumsets[0]
        datum = datumset[0]
        expected_data = {
            "Person": {
                "Time:2012": {
                    "District:LK-11": {
                        "Religion:Buddhist": {"Count": "Int:1632125"}
                    }
                }
            }
        }
        self.assertEqual(datum.to_data(), expected_data)
