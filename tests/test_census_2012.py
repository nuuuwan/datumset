import unittest

from ds.db.Census2012 import Census2012


class TestCase(unittest.TestCase):
    def test_basic(self):
        datumset = Census2012.get_religion()
        expected = {
            "Person": {
                "Time:2012": {
                    "District:LK-11": {
                        "Religion:Buddhist": {"Count": "Int:1632125"}
                    }
                }
            }
        }
        self.assertEqual(
            [datum.to_data() for datum in datumset].count(expected),
            1,
        )
