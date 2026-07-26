import unittest

from ds import LankaData, Query, VisualFactory


class TestCase(unittest.TestCase):
    def test_method(self):
        query_str_list = ["Person/Time*Country*Religion/Count"]
        visual_class_names = ["BarChart"]

        for query_str in query_str_list:
            for visual_class_name in visual_class_names:
                with self.subTest(
                    query_str=query_str, visual_class_name=visual_class_name
                ):

                    datumset = LankaData[query_str]
                    VisualClass = VisualFactory[visual_class_name]

                    query = Query(query_str)
                    visual = VisualClass(
                        datumset, query.dim_labels[0], query.cell_labels[0]
                    )
                    visual.draw()
                    self.assertTrue(visual.image_file.exists())
