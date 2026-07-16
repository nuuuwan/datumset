import unittest

from ds.thing.concept.Religion import Religion


class TestCase(unittest.TestCase):
    def test_invalid_label(self):
        with self.assertRaises(ValueError):
            concept = Religion["SriLankan"]
            self.assertIsNone(concept)
