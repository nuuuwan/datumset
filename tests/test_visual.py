import unittest

from ds import LankaData, VisualFactory


class TestCase(unittest.TestCase):
    def test_method(self):

        datumset = LankaData["Person/Time*Province*Religion/Count"]
        visual = VisualFactory["BarChart"](datumset, "Religion", "Count")
        visual.draw()
        self.assertTrue(visual.image_file.exists())
