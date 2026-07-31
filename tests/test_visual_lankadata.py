import os
import re
import unittest

from utils_future import YAMLFile

from ds import VisualLankaData

DATA_PATH = os.path.join(
    os.path.dirname(__file__), "test_visual_lankadata.data.yaml"
)


class TestCase(unittest.TestCase):

    @staticmethod
    def get_query_strs():
        query_strs_file = YAMLFile(DATA_PATH)
        query_strs = query_strs_file.read()
        for query_str in query_strs:
            tokens = query_str.split("/")
            if len(tokens) != 4:
                raise ValueError(f"Invalid query string: {query_str}")
        query_strs = list(set(query_strs))
        query_strs.sort()
        lines = []
        prev_first_token = None
        for query_str in query_strs:
            first_token = query_str.split("/")[0]
            if first_token != prev_first_token:
                lines.extend([f"# {prev_first_token}"])
            lines.append(f"- {query_str}")
            prev_first_token = first_token
        query_strs_file.write_lines(lines)
        return query_strs

    @staticmethod
    def build_test(visual_query_str):
        def test(self):
            image_file = VisualLankaData[visual_query_str]
            self.assertTrue(image_file.exists())
            expected_path = os.path.join("images", visual_query_str + ".png")
            self.assertEqual(image_file.path, expected_path)

        return test


for i, scenario in enumerate(TestCase.get_query_strs()):
    cleaned_scenario = re.sub(r"[^0-9a-zA-Z_]+", "_", scenario)
    test_name = f"test_{i}_{cleaned_scenario}"
    setattr(TestCase, test_name, TestCase.build_test(scenario))
