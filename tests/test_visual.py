import unittest

from ds import LankaData, VisualFactory


class TestCase(unittest.TestCase):
    def test_method(self):
        query_str_list = ["Person/Time*Province*Religion/Count"]

        for query_str in query_str_list:
            for VisualClass in VisualFactory.visual_class_list():
                with self.subTest(
                    query_str=query_str,
                    visual_class_name=VisualClass.__name__,
                ):

                    datumset = LankaData[query_str]

                    visual = VisualClass(datumset)
                    visual.draw()
                    self.assertTrue(visual.image_file.exists())
