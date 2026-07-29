import json
import os
import unittest

from ds import Datumset

DIR_DATA = os.path.join(os.path.dirname(__file__), "data")


class TestCase(unittest.TestCase):

    def _get_data(self):
        path = os.path.join(DIR_DATA, "test_datumset.json")
        with open(path) as fin:
            return json.load(fin)

    def test_split(self):
        data = self._get_data()
        datumset = Datumset.from_data(data["input"])

        split_datumsets = datumset.split("Time")

        self.assertEqual(len(split_datumsets), 2)
        self.assertEqual(split_datumsets[0].to_data(), data["split"][0])
        self.assertEqual(split_datumsets[1].to_data(), data["split"][1])
