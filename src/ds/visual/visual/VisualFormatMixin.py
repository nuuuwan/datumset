from matplotlib.ticker import FuncFormatter
from utils_future import Int

from ds.thing.concept.atom.Int import Int as IntConcept
from ds.thing.concept.atom.Percent import Percent as PercentConcept


class VisualFormatMixin:

    OTHER_CATEGORY_LABEL = "Other"

    def _format_visual_value(self, value):
        if value == self.OTHER_CATEGORY:
            return self.OTHER_CATEGORY_LABEL
        normalized = value.replace("_", " ").strip()
        if normalized.islower() and any(c.isalpha() for c in normalized):
            return normalized.title()
        return value

    def _format_humanized_value(self, value, _pos):
        return Int(int(round(value, 0))).humanize

    def _format_humanized_y_axis(self, ax):
        formatter = FuncFormatter(self._format_humanized_value)
        ax.yaxis.set_major_formatter(formatter)

    def _format_cell_value_for_axis(self, cell_key, value, _pos):
        cell = self._get_cell_concept(cell_key) if cell_key else None
        if isinstance(cell, PercentConcept):
            return f"{value:.1f}%"
        if cell is None or isinstance(cell, IntConcept):
            return Int(int(round(value, 0))).humanize
        return f"{value:.2g}"

    def _format_cell_y_axis(self, ax, cell_key):
        fmt = FuncFormatter(
            lambda v, p: self._format_cell_value_for_axis(cell_key, v, p)
        )
        ax.yaxis.set_major_formatter(fmt)

    def _format_y_value(self, value):
        cell_key = getattr(self, 'y_cell_key', None)
        return self._format_cell_value_for_axis(cell_key, float(value), None)
