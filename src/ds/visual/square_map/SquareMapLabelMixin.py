from ds.visual.hex_map.HexMapLabelMixin import HexMapLabelMixin
from ds.visual.square_map.SquareTextFit import SquareTextFit


class SquareMapLabelMixin(HexMapLabelMixin):

    def _best_label_fit(self, points, radius):
        return SquareTextFit.best_label_fit(points, radius)
