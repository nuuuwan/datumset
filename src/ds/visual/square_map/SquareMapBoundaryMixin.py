from shapely.geometry import Polygon

from ds.visual.hex_map.HexMapBoundaryMixin import HexMapBoundaryMixin


class SquareMapBoundaryMixin(HexMapBoundaryMixin):

    @staticmethod
    def _hex_polygon(x, y, radius):
        return Polygon(
            [
                (x - radius, y - radius),
                (x + radius, y - radius),
                (x + radius, y + radius),
                (x - radius, y + radius),
            ]
        )
