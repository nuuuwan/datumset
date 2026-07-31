import unittest
from unittest.mock import MagicMock

from ds.visual.visual.VisualXAxisMixin import VisualXAxisMixin


class _TestVisual(VisualXAxisMixin):

    def __init__(self):
        self.x_dim_key = "X"
        self._renderer = None

    def _format_visual_value(self, value):
        return str(value)

    def _can_shorten_dim(self, dim_key):
        return True


class _TestVisualUnshortenable(VisualXAxisMixin):

    def __init__(self):
        self.x_dim_key = "X"
        self._renderer = None

    def _format_visual_value(self, value):
        return str(value)

    def _can_shorten_dim(self, dim_key):
        return False


class TestCase(unittest.TestCase):

    def test_wrap_x_label_short_lines(self):
        visual = _TestVisualUnshortenable()
        label = "household work or childcare"
        self.assertEqual(
            visual._wrap_x_label(label, 20),
            "household work or\nchildcare",
        )

    def test_wrap_x_label_long_word(self):
        visual = _TestVisualUnshortenable()
        label = "uncharacteristically_long_word"
        wrapped = visual._wrap_x_label(label, 10)
        self.assertEqual(wrapped, label)

    def test_wrap_x_label_no_break_needed(self):
        visual = _TestVisualUnshortenable()
        label = "short"
        self.assertEqual(visual._wrap_x_label(label, 20), "short")

    def test_shorten_x_label_when_shortenable(self):
        visual = _TestVisual()
        sub_ax = MagicMock()
        sub_ax.figure.dpi = 100
        label = "household work or childcare"
        result = visual._shorten_x_label(sub_ax, label, 30)
        self.assertEqual(result, "HWOC")
