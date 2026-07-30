import re
import unittest

from utils_future import JSONFile

from ds import VisualLankaData


class TestCase(unittest.TestCase):

    @staticmethod
    def get_scenarios():
        return JSONFile("tests", "test_visual_lankadata.data.json").read()

    @staticmethod
    def build_test(visual_query_str):
        def test(self):
            image_file = VisualLankaData[visual_query_str]
            self.assertTrue(image_file.exists())

        return test


for i, scenario in enumerate(TestCase.get_scenarios()):
    cleaned_scenario = re.sub(r"[^0-9a-zA-Z_]+", "_", scenario)
    test_name = f"test_{i}_{cleaned_scenario}"
    setattr(TestCase, test_name, TestCase.build_test(scenario))
