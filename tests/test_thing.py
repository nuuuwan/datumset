import unittest

from ds.thing.concept.Religion import Religion
from ds.thing.ThingFactory import ThingFactory


class TestCase(unittest.TestCase):

    def test_invalid_thing(self):
        with self.assertRaises(ValueError):
            class_for_label = ThingFactory["Invalid"]
            self.assertIsNone(class_for_label)

    def test_invalid_label(self):
        with self.assertRaises(ValueError):
            concept = Religion["SriLankan"]
            self.assertIsNone(concept)
