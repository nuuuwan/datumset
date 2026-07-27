import glob
import math
import os
from abc import ABC, abstractmethod
from functools import cached_property

import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from utils_future import Directory, File, Log

from ds.query.Query import Query

log = Log("Visual")

_FONTS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "media", "fonts"
)
for _ttf in glob.glob(os.path.join(_FONTS_DIR, "**", "*.ttf")):
    fm.fontManager.addfont(_ttf)


class Visual(ABC):

    FIGSIZE = (9, 9)
    DPI = 100
    STRIP_COLOR = "#e8e8e8"
    BORDER_COLOR = "#cccccc"
    TITLE_COLOR = "#333333"
    SUBTITLE_COLOR = "#555555"
    DIR_FONTS = os.path.join("media", "fonts", "Fira_Sans")
    FONT_FAMILY = "Fira Sans"
    FONT_SIZE = 8

    def __init__(self, datumset, *params):
        self.datumset = datumset
        self.params = params

    def _get_query_str_for_path(self):
        query = self.datumset[0].query
        dim_specs = []
        for dim_label in query.dim_labels:
            dim_values = self._get_unique_dim_values(dim_label)
            if len(dim_values) == 1:
                dim_specs.append(f"{dim_label}={dim_values[0]}")
                continue
            dim_specs.append(dim_label)
        dim_part = Query.OPR_MULT.join(dim_specs)
        return Query.DELIM_PART.join(
            [
                query.entity_part,
                dim_part,
                query.cell_part,
            ]
        )

    @cached_property
    def dir_visual(self) -> Directory:
        query_str_for_path = self._get_query_str_for_path()
        dir_visual = Directory("images", query_str_for_path)
        dir_visual.make()
        return dir_visual

    @cached_property
    def image_file(self) -> File:
        return File(self.dir_visual, self.__class__.__name__ + ".png")

    def _excluded_dim_keys(self):
        return set()

    def _get_dim_labels(self):
        return self.datumset[0].query.dim_labels

    def _get_display_datumsets(self, excluded_dim_keys):
        split_dims = [
            dim_key
            for dim_key in self._get_dim_labels()
            if dim_key not in excluded_dim_keys
        ]
        if not split_dims:
            return [self.datumset]
        return self.datumset.split(*split_dims)

    def _get_unique_dim_values(self, dim_key):
        values = []
        for datum in self.datumset:
            value = datum.dim_idx[dim_key].get_value()
            if value not in values:
                values.append(value)
        return values

    def _get_subfigure_title(self, datumset, excluded_dim_keys):
        constant_parts = []
        first_datum = datumset[0]
        for dim_key in first_datum.query.dim_labels:
            if dim_key in excluded_dim_keys:
                continue
            first_value = first_datum.dim_idx[dim_key].get_value()
            if all(
                datum.dim_idx[dim_key].get_value() == first_value
                for datum in datumset
            ):
                constant_parts.append(f"{dim_key}: {first_value}")
        if constant_parts:
            return "\n".join(constant_parts)
        return "All data"

    def _build_subtitle(self):
        datum = self.datumset[0]
        entity = datum.entity_class.__name__
        other = [
            f"{k}: {v.get_value()}"
            for k, v in datum.dim_idx.items()
            if k not in self._excluded_dim_keys()
        ]
        return " | ".join([entity] + other)

    @abstractmethod
    def _build_title(self):
        pass

    @abstractmethod
    def _plot(self, fig, ax):
        pass

    def _get_title_text(self):
        datum = self.datumset[0]
        entity = datum.entity_class.__name__
        other = [
            f"{k} {v.get_value()}"
            for k, v in datum.dim_idx.items()
            if k not in self._excluded_dim_keys()
        ]
        suffix = " for " + " and ".join(other) if other else ""
        return f"{entity} {self._build_title()}{suffix}"

    def _add_title(self, fig):
        title = self._get_title_text()
        fig.text(
            0.5,
            0.95,
            title,
            ha="center",
            va="center",
            fontsize=12 * (100 / len(title)),
            color=self.TITLE_COLOR,
            zorder=6,
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
            ax.tick_params(colors=self.SUBTITLE_COLOR)
        SUBPLOT_PADDING = 0.15
        fig.subplots_adjust(
            top=1 - SUBPLOT_PADDING,
            bottom=SUBPLOT_PADDING,
            left=SUBPLOT_PADDING,
            right=1 - SUBPLOT_PADDING,
            hspace=1.0,
            wspace=0.8,
        )

    def _get_square_axes(self, fig, ax, n_subfigures):
        if n_subfigures == 1:
            return [ax]
        fig.clear()
        n_side = math.ceil(math.sqrt(n_subfigures))
        axes = fig.subplots(nrows=n_side, ncols=n_side)
        return axes.flatten()

    def _hide_empty_axes(self, axes, n_subfigures):
        for empty_ax in axes[n_subfigures:]:
            empty_ax.set_visible(False)

    def _format_humanized_value(self, value, _pos):
        abs_value = abs(value)
        formatted_value = None
        if abs_value >= 1000000:
            formatted_value = self._format_humanized_scaled(
                value / 1000000,
                "M",
            )
        elif abs_value >= 1000:
            formatted_value = self._format_humanized_scaled(value / 1000, "K")
        elif value.is_integer():
            formatted_value = str(int(value))
        else:
            formatted_value = f"{value:g}"
        return formatted_value

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

    def _add_color_legend(self, fig, value_color_idx, title):
        legend_handles = [
            mpatches.Patch(color=color, label=value)
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

    def draw(self):
        self._set_font()
        fig, ax = plt.subplots(figsize=self.FIGSIZE, dpi=self.DPI)
        self._plot(fig, ax)
        self._add_title(fig)
        self._add_border(fig)
        self._apply_style(fig, fig.axes)
        fig.savefig(self.image_file.path)
        log.debug(f"Wrote {self.image_file}")
        plt.close(fig)
        return fig
