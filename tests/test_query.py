import unittest

from ds.query.Query import Query


class TestCase(unittest.TestCase):
    def test_basic(self):
        query = Query("Person/Time*District*Religion/Count")

        self.assertEqual(query.entity_class_names, ["Person"])
        self.assertEqual(query.dim_labels, ["Time", "District", "Religion"])
        self.assertEqual(query.cell_labels, ["Count"])
