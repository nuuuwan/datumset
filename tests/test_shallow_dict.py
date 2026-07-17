import unittest

from utils_future import ShallowDict


class TestCase(unittest.TestCase):
    def test_basic(self):
        d = ShallowDict()

        for k, v, e_deep_d in [
            [
                ("a",),
                1,
                {"a": 1},
            ],
            [
                ("a",),
                {"b": 2},
                {"a": {"b": 2}},
            ],
            [
                ("a", "b", "c"),
                {"d": 1, "e": 2},
                {"a": {"b": {"c": {"d": 1, "e": 2}}}},
            ],
            [
                ("a", "b", "c"),
                {"d": 1},
                {"a": {"b": {"c": {"d": 1}}}},
            ],
        ]:
            d[k] = v

            deep_d = d.to_deep()
            self.assertEqual(deep_d, e_deep_d)

            d2 = ShallowDict.from_deep(deep_d)
            self.assertEqual(d, d2)
