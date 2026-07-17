import unittest

from ds.thing.concept.region.RegionFactory import RegionFactory
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

    def test_region_factory_invlid(self):
        with self.assertRaises(ValueError):
            region_cls = RegionFactory.from_region_id("EC-01AA")
            self.assertIsNone(region_cls)
        with self.assertRaises(ValueError):
            region_cls = RegionFactory.from_region_id("LK-123456789012345")
            self.assertIsNone(region_cls)
        with self.assertRaises(ValueError):
            region_cls = RegionFactory.from_region_id("XXXXXX")
            self.assertIsNone(region_cls)
