from matplotlib.ticker import FuncFormatter
from utils_future import Int


class VisualFormatMixin:

    def _format_visual_value(self, value):
        if value == self.OTHER_CATEGORY:
            return self.OTHER_CATEGORY_LABEL
        if not isinstance(value, str):
            return value
        return self._titleize_value(value)

    def _titleize_value(self, value):
        normalized = value.replace("_", " ").strip()
        if normalized.islower() and any(c.isalpha() for c in normalized):
            return normalized.title()
        return value

    def _format_humanized_value(self, value, _pos):
        return Int(value).humanize

    def _format_humanized_y_axis(self, ax):
        formatter = FuncFormatter(self._format_humanized_value)
        ax.yaxis.set_major_formatter(formatter)
