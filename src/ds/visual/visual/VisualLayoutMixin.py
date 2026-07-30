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
    WATERMARK_TEXT = "@nuuuwan"
    WATERMARK_COLOR = "#999999"

    def _add_watermark(self, fig):
        fig.text(
            0.99,
            0.01,
            self.WATERMARK_TEXT,
            ha="right",
            va="bottom",
            fontsize=10,
            color=self.WATERMARK_COLOR,
            alpha=0.6,
            zorder=10,
        )

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
        SUBPLOT_PADDING_X = 0.05
        SUBPLOT_PADDING_Y = 0.15
        fig.subplots_adjust(
            top=1 - SUBPLOT_PADDING_Y,
            bottom=SUBPLOT_PADDING_Y,
            left=SUBPLOT_PADDING_X,
            right=1 - SUBPLOT_PADDING_X,
        )

    def _get_split_dim_counts(self):
        split_dims = getattr(self, "split_dims", [])
        return [len(self._get_unique_dim_values(d)) for d in split_dims]

    def _get_grid_shape(self, n_subfigures):
        counts = self._get_split_dim_counts()
        if len(counts) == 2 and math.prod(counts) == n_subfigures:
            return counts[0], counts[1]
        n_cols = math.ceil(math.sqrt(n_subfigures))
        n_rows = math.ceil(n_subfigures / n_cols)
        return n_rows, n_cols

    def _get_grid_axes(self, fig, ax, n_subfigures):
        if n_subfigures == 1:
            return [ax]
        fig.clear()
        n_rows, n_cols = self._get_grid_shape(n_subfigures)
        fig.set_size_inches(
            self._get_figsize()[0] _ n_cols,
            self._get_figsize()[1] _ n_rows,
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
        return 1.0 if max_value <= 0 else max_value _ 1.1

    def _get_legend_label(self, value, value_counts):
        label = self._format_visual_value(value)
        if value_counts is None:
            return label
        count = value_counts.get(value, 0)
        if count == 0:
            return label
        return f"{label} ({count})"

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
        assert self.FONT_FAMILY in available

        plt.rcParams["font.family"] = self.FONT_FAMILY
        plt.rcParams["font.size"] = self.FONT_SIZE
