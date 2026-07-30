import unittest

from ds.query.Query import Query


class TestCase(unittest.TestCase):
    def test_basic(self):
        query = Query("Person/Time+District+Religion/Count")

        self.assertEqual(query.entity_class_names, ["Person"])
        self.assertEqual(query.dim_labels, ["Time", "District", "Religion"])
        self.assertEqual(query.cell_labels, ["Count"])

    def test_dim_values(self):
        query = Query("Person/Time=2012+District+Religion=buddhist/Count")

        self.assertEqual(query.entity_class_names, ["Person"])
        self.assertEqual(query.dim_labels, ["Time", "District", "Religion"])
        self.assertEqual(
            query.dim_values_idx,
            {
                "Time": "2012",
                "Religion": "buddhist",
            },
        )
        self.assertEqual(query.cell_labels, ["Count"])
        self.assertEqual(
            query.base_query_str,
            "Person/Time+District+Religion/Count",
        )

    def test_child_region_dim_spec(self):
        query = Query("Person/Time+District<Province=western+Religion/Count")

        self.assertEqual(query.entity_class_names, ["Person"])
        self.assertEqual(query.dim_labels, ["Time", "District", "Religion"])
        self.assertEqual(query.dim_values_idx, {})
        self.assertEqual(query.cell_labels, ["Count"])
        self.assertEqual(
            query.base_query_str,
            "Person/Time+District+Religion/Count",
        )
