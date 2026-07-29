from matplotlib.patches import Rectangle

from ds.visual.hex_map.HexMapDrawMixin import HexMapDrawMixin


class SquareMapDrawMixin(HexMapDrawMixin):

    def _draw_hex(self, ax, x, y, radius, color):
        ax.add_patch(
            Rectangle(
                (x - radius, y - radius),
                2 * radius,
                2 * radius,
                facecolor=color,
                edgecolor=self.HEX_EDGE_COLOR,
                linewidth=self.HEX_EDGE_WIDTH,
            )
        )
