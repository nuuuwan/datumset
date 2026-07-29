from matplotlib.ticker import FuncFormatter
from utils_future import Int


class VisualFormatMixin:

    def _build_dim_title(self, y_cell_key, dim_key, relation="by"):
        return f"{y_cell_key} {relation} {dim_key}"

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

    def _format_humanized_scaled(self, scaled_value, suffix):
        abs_scaled_value = abs(scaled_value)
        if abs_scaled_value >= 100:
            display_value = int(scaled_value)
            return f"{display_value}{suffix}"
        display_value = int(scaled_value * 10) / 10
        return f"{display_value:.1f}{suffix}"

    def _format_humanized_y_axis(self, ax):
        formatter = FuncFormatter(self._format_humanized_value)
        ax.yaxis.set_major_formatter(formatter)

    def _format_percentage_value(self, value, total):
        if total <= 0:
            return "0%"
        pct = value * 100.0 / total
        if pct > 0.5:
            return f"{pct:.0f}%"
        return "<0.5%"
