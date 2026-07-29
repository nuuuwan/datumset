class MarimekkoGeometryMixin:

    BAR_HEIGHT = 1.0
    BAR_GAP = 0.01

    def _get_available_width(self, n_bars):
        gaps = self.BAR_GAP * max(n_bars - 1, 0)
        available = 1.0 - gaps
        return available, self.BAR_GAP

    def _get_bar_geometry(self, totals):
        grand_total = sum(totals) or 1.0
        available, gap = self._get_available_width(len(totals))
        geometry = []
        left = 0.0
        for total in totals:
            width = available * total / grand_total
            geometry.append((left, width))
            left += width + gap
        return geometry

    def _get_segment_height(self, value, total):
        return self.BAR_HEIGHT * value / total
