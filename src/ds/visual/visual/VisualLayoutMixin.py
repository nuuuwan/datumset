import math
import os

import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


class VisualLayoutMixin:

    BORDER_COLOR = "#cccccc"
    SUBTITLE_COLOR = "#555555"
    DIR_FONTS = os.path.join("media", "fonts", "Fira_Sans")
    FONT_FAMILY = "Fira Sans"
    FONT_SIZE = 8

    def _add_border(self, fig):
        border = mpatches.Rectangle(
            (0.0, 0.0),
            1,
            1,
            transform=fig.transFigure,
            fill=False,
            edgecolor=self.BORDER_COLOR,
            linewidth=2,
            zorder=5,
            clip_on=False,
        )
        fig.add_artist(border)

    def _apply_style(self, fig, axes):
        for ax in axes:
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_color(self.BORDER_COLOR)
            ax.spines["bottom"].set_color(self.BORDER_COLOR)
            ax.tick_params(axis="y", colors=self.SUBTITLE_COLOR)
            ax.tick_params(axis="x", color=self.SUBTITLE_COLOR)
        SUBPLOT_PADDING = 0.025
        fig.subplots_adjust(
            top=1 - SUBPLOT_PADDING,
            bottom=SUBPLOT_PADDING,
            left=SUBPLOT_PADDING,
            right=1 - SUBPLOT_PADDING,
            hspace=1.0,
            wspace=0.8,
        )

    def _get_grid_axes(self, fig, ax, n_subfigures):
        if n_subfigures == 1:
            return [ax]
        fig.clear()
        n_cols = math.ceil(math.sqrt(n_subfigures))
        n_rows = math.ceil(n_subfigures / n_cols)
        fig.set_size_inches(
            self.FIGSIZE[0] * n_cols,
            self.FIGSIZE[1] * n_rows,
        )
        axes = fig.subplots(nrows=n_rows, ncols=n_cols)
        return axes.flatten()

    def _get_display_axes(self, fig, ax, display_datumsets):
        n_subfigures = len(display_datumsets)
        axes = self._get_grid_axes(fig, ax, n_subfigures)
        return axes, n_subfigures

    def _hide_empty_axes(self, axes, n_subfigures):
        for empty_ax in axes[n_subfigures:]:
            empty_ax.set_visible(False)

    def _get_y_axis_limit(self, max_value):
        return 1.0 if max_value <= 0 else max_value * 1.1

    def _get_legend_label(self, value, value_counts):
        label = self._format_visual_value(value)
        if value_counts is None:
            return label
        return f"{label} ({value_counts.get(value, 0)})"

    def _add_color_legend(
        self, fig, value_color_idx, title, value_counts=None
    ):
        legend_handles = [
            mpatches.Patch(
                color=color,
                label=self._get_legend_label(value, value_counts),
            )
            for value, color in value_color_idx.items()
        ]
        fig.legend(
            handles=legend_handles,
            title=title,
            loc="lower center",
            bbox_to_anchor=(0.5, 0.01),
            ncol=min(4, len(legend_handles)),
            frameon=False,
        )

    def _set_font(self):
        for file in os.listdir(self.DIR_FONTS):
            if file.endswith(".ttf"):
                fm.fontManager.addfont(os.path.join(self.DIR_FONTS, file))
        available = [f.name for f in fm.fontManager.ttflist]
        if self.FONT_FAMILY not in available:
            raise ValueError(f"Font '{self.FONT_FAMILY}' not available")

        plt.rcParams["font.family"] = self.FONT_FAMILY
        plt.rcParams["font.size"] = self.FONT_SIZE
