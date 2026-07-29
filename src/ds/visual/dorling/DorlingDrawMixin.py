from matplotlib.patches import Circle


class DorlingDrawMixin:

    CIRCLE_EDGE_COLOR = "#ffffff"
    CIRCLE_EDGE_WIDTH = 1.0

    def _draw_circle(self, ax, xy, radius, color):
        ax.add_patch(
            Circle(
                xy,
                radius,
                facecolor=color,
                edgecolor=self.CIRCLE_EDGE_COLOR,
                linewidth=self.CIRCLE_EDGE_WIDTH,
            )
        )

    def _draw_circles(self, ax, circles, region_color):
        for region_id, (x, y), radius in circles:
            color = region_color.get(region_id, "#cccccc")
            self._draw_circle(ax, (x, y), radius, color)

    def _set_limits(self, ax, circles):
        if not circles:
            return
        xmin = min(c[1][0] - c[2] for c in circles)
        xmax = max(c[1][0] + c[2] for c in circles)
        ymin = min(c[1][1] - c[2] for c in circles)
        ymax = max(c[1][1] + c[2] for c in circles)
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        ax.set_aspect("equal")
        ax.set_axis_off()

    def _plot_subfigure(self, fig, sub_ax, sub_datumset, ctx):
        gdf = self._get_colored_gdf(sub_datumset, ctx)
        region_color = dict(zip(gdf["region_id"], gdf["color"]))
        circles = self._get_circles(gdf)
        self._draw_circles(sub_ax, circles, region_color)
        self._set_limits(sub_ax, circles)
        self._add_circle_labels(fig, sub_ax, circles, gdf)
        self._set_square_subfigure_title(sub_ax, sub_datumset)
