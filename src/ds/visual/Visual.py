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
    DPI = 300
    STRIP_COLOR = "#e8e8e8"
    BORDER_COLOR = "#cccccc"
    TITLE_COLOR = "#333333"
    SUBTITLE_COLOR = "#555555"
    DIR_FONTS = os.path.join("media", "fonts", "Fira_Sans")
    FONT_FAMILY = "Fira Sans"
    FONT_SIZE = 8
    MIN_STACK_LABEL_FONTSIZE = 8
    MAX_STACK_LABEL_FONTSIZE = 20
    STACK_LABEL_FONT_REDUCTION = 1
    STACK_LABEL_MIN_DIM_RATIO = 0.55
    STACK_LABEL_BBOX_MARGIN = 0.75

    def __init__(self, datumset, *params):
        self.datumset = datumset
        self.params = params

    def _get_query(self):
        return self.datumset[0].query

    def _get_entity_name(self):
        return self.datumset[0].entity_class.__name__

    def _resolve_dim_key(self, dim_key, default_index):
        if dim_key is not None:
            return dim_key
        return self._get_query().dim_labels[default_index]

    def _resolve_cell_key(self, cell_key, default_index=0):
        if cell_key is not None:
            return cell_key
        return self._get_query().cell_labels[default_index]

    def _init_dim_colors(self, dim_key):
        dim_values = self._get_unique_dim_values(dim_key)
        color_idx = self._get_dim_color_idx(dim_key, dim_values)
        return dim_values, color_idx

    def _build_dim_title(self, y_cell_key, dim_key):
        return f"{y_cell_key} by {dim_key}"

    def _build_entity_dim_title(self, y_cell_key, dim_key, relation="by"):
        return f"{self._get_entity_name()} {y_cell_key} {relation} {dim_key}"

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

    def _get_dim_cell_xy(self, datumset, dim_key, cell_key):
        x_labels = []
        y_values = []
        for datum in datumset:
            x_labels.append(datum.dim_idx[dim_key].get_value())
            y_values.append(float(datum.cell_idx[cell_key].get_value()))
        return x_labels, y_values

    def _format_visual_value(self, value):
        if not isinstance(value, str):
            return value
        normalized = value.replace("_", " ")
        if normalized.islower() and any(c.isalpha() for c in normalized):
            return normalized.title()
        return value

    def _get_default_color_idx(self, dim_values):
        cmap = plt.get_cmap("tab20")
        return {
            dim_value: cmap(i % cmap.N)
            for i, dim_value in enumerate(dim_values)
        }

    def _get_dim_color_map(self, dim_key):
        concept = self.datumset[0].dim_idx.get(dim_key)
        color_map = None
        if concept is not None:
            concept_class = concept.__class__
            get_color_map = getattr(concept_class, "get_color_map", None)
            if get_color_map is not None:
                maybe_color_map = get_color_map()
                if isinstance(maybe_color_map, dict):
                    color_map = maybe_color_map
        return color_map

    def _get_dim_color_idx(self, dim_key, dim_values):
        default_color_idx = self._get_default_color_idx(dim_values)
        color_map = self._get_dim_color_map(dim_key)
        if not color_map:
            return default_color_idx
        return {
            dim_value: color_map.get(dim_value, default_color_idx[dim_value])
            for dim_value in dim_values
        }

    def _get_fixed_dim_color(self, dim_key):
        dim_values = self._get_unique_dim_values(dim_key)
        if len(dim_values) != 1:
            return None
        color_map = self._get_dim_color_map(dim_key)
        if not color_map:
            return None
        dim_value = dim_values[0]
        return color_map.get(dim_value)

    def _get_single_fixed_dim_color(self, excluded_dim_keys=None):
        excluded_dim_keys = excluded_dim_keys or set()
        for dim_key in self._get_dim_labels():
            if dim_key in excluded_dim_keys:
                continue
            color = self._get_fixed_dim_color(dim_key)
            if color is not None:
                return color
        return None

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
                display_value = self._format_visual_value(first_value)
                constant_parts.append(f"{dim_key}: {display_value}")
        if constant_parts:
            return "\n".join(constant_parts)
        return "All data"

    def _set_subfigure_title(self, sub_ax, sub_datumset):
        sub_ax.set_title(
            self._get_subfigure_title(
                sub_datumset,
                self._excluded_dim_keys(),
            ),
            fontsize=7,
            pad=3,
        )

    def _style_value_axis_subfigure(
        self,
        sub_ax,
        y_cell_key,
        y_limit,
        sub_datumset,
        x_labels=None,
    ):
        sub_ax.set_ylabel(y_cell_key)
        sub_ax.set_ylim(0, y_limit)
        self._format_humanized_y_axis(sub_ax)
        if x_labels:
            display_x_labels = [
                self._format_visual_value(x_label) for x_label in x_labels
            ]
            sub_ax.set_xticks(range(len(x_labels)))
            sub_ax.set_xticklabels(display_x_labels, fontsize=6)
        else:
            sub_ax.set_xticks([])
        sub_ax.set_box_aspect(1)
        self._set_subfigure_title(sub_ax, sub_datumset)

    def _set_square_subfigure_title(self, sub_ax, sub_datumset):
        sub_ax.set_box_aspect(1)
        self._set_subfigure_title(sub_ax, sub_datumset)

    def _build_subtitle(self):
        datum = self.datumset[0]
        entity = datum.entity_class.__name__
        other = [
            f"{k}: {self._format_visual_value(v.get_value())}"
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
            f"{k} {self._format_visual_value(v.get_value())}"
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

    def _get_display_axes(self, fig, ax, display_datumsets):
        n_subfigures = len(display_datumsets)
        axes = self._get_square_axes(fig, ax, n_subfigures)
        return axes, n_subfigures

    def _hide_empty_axes(self, axes, n_subfigures):
        for empty_ax in axes[n_subfigures:]:
            empty_ax.set_visible(False)

    def _get_y_axis_limit(self, max_value):
        return 1.0 if max_value <= 0 else max_value * 1.1

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

    def _format_percentage_value(self, value, total):
        if total <= 0:
            return "0%"
        pct = value * 100.0 / total
        if pct > 0.5:
            return f"{pct:.0f}%"
        return "<0.5%"

    def _add_bar_totals(self, sub_ax, x_values, totals, y_limit):
        offset = y_limit * 0.015
        for x_value, total in zip(x_values, totals):
            sub_ax.text(
                x_value,
                total + offset,
                self._format_humanized_value(float(total), None),
                ha="center",
                va="bottom",
                fontsize=7,
                color=self.SUBTITLE_COLOR,
            )

    def _get_rect_size_px(self, sub_ax, rect):
        x0 = rect.get_x()
        y0 = rect.get_y()
        x1 = x0 + rect.get_width()
        y1 = y0 + rect.get_height()
        px0, py0 = sub_ax.transData.transform((x0, y0))
        px1, py1 = sub_ax.transData.transform((x1, y1))
        return abs(px1 - px0), abs(py1 - py0)

    def _get_rect_fontsize_cap(self, sub_ax, rect):
        max_width_px, max_height_px = self._get_rect_size_px(sub_ax, rect)
        min_dim_px = min(max_width_px, max_height_px)
        px_to_pt = 72.0 / sub_ax.figure.dpi
        return int(min_dim_px * px_to_pt * self.STACK_LABEL_MIN_DIM_RATIO)

    def _get_best_rect_label_fontsize(self, sub_ax, rect, label):
        fig = sub_ax.figure
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        cx = rect.get_x() + rect.get_width() / 2.0
        cy = rect.get_y() + rect.get_height() / 2.0
        max_width_px, max_height_px = self._get_rect_size_px(sub_ax, rect)
        fontsize_cap = self._get_rect_fontsize_cap(sub_ax, rect)
        if fontsize_cap < self.MIN_STACK_LABEL_FONTSIZE:
            return 0
        probe = sub_ax.text(cx, cy, label, ha="center", va="center")
        best_fontsize = 0
        max_fontsize = min(self.MAX_STACK_LABEL_FONTSIZE, fontsize_cap)
        for fontsize in range(max_fontsize, 3, -1):
            probe.set_fontsize(fontsize)
            bbox = probe.get_window_extent(renderer=renderer)
            if (
                bbox.width <= max_width_px * self.STACK_LABEL_BBOX_MARGIN
                and bbox.height
                <= max_height_px * self.STACK_LABEL_BBOX_MARGIN
            ):
                best_fontsize = fontsize
                break
        probe.remove()
        return best_fontsize

    def _add_fitted_label_in_rect(self, sub_ax, rect, label):
        fontsize = self._get_best_rect_label_fontsize(sub_ax, rect, label)
        fontsize -= self.STACK_LABEL_FONT_REDUCTION
        if fontsize < self.MIN_STACK_LABEL_FONTSIZE:
            return
        cx = rect.get_x() + rect.get_width() / 2.0
        cy = rect.get_y() + rect.get_height() / 2.0
        sub_ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            fontsize=fontsize,
            color="white",
        )

    def _add_stacked_bar_percentages(self, sub_ax, bars, values, totals):
        for i, rect in enumerate(bars):
            value = values[i]
            total = totals[i]
            if value <= 0 or total <= 0:
                continue
            label = self._format_percentage_value(value, total)
            self._add_fitted_label_in_rect(sub_ax, rect, label)

    def _add_color_legend(self, fig, value_color_idx, title):
        legend_handles = [
            mpatches.Patch(
                color=color,
                label=self._format_visual_value(value),
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

    def draw(self):
        self._set_font()
        fig, ax = plt.subplots(figsize=self.FIGSIZE, dpi=self.DPI)
        self._plot(fig, ax)
        self._add_title(fig)
        self._add_border(fig)
        self._apply_style(fig, fig.axes)
        fig.savefig(self.image_file.path, dpi=self.DPI, bbox_inches="tight")
        log.debug(f"Wrote {self.image_file}")
        plt.close(fig)
        return fig
