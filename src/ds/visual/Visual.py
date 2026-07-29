import glob
import math
import os
from abc import ABC, abstractmethod
from collections import defaultdict
from functools import cached_property

import matplotlib.colors as mcolors
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from utils_future import Directory, File, Int, Log

from ds.query.Query import Query
from ds.thing.concept.region.Region import Region

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
    CONTRAST_LIGHT_TEXT_COLOR = "#ffffff"
    CONTRAST_DARK_TEXT_COLOR = "#111111"
    CONTRAST_LIGHTNESS_THRESHOLD = 0.5
    OTHER_CATEGORY = "_other"
    SMALL_CATEGORY_THRESHOLD = 0.01
    OTHER_CATEGORY_COLOR = "#999999"
    OTHER_CATEGORY_LABEL = "Other (with <1%)"

    def __init__(self, datumset):
        self.datumset = datumset
        self.params = self._get_params()

    def _get_params(self):
        return ()

    def _get_query(self):
        return self.datumset[0].query

    def _get_entity_name(self):
        return self.datumset[0].entity_class.__name__

    def _get_dim_concept(self, dim_key):
        return self.datumset[0].dim_idx.get(dim_key)

    def _is_region_dim(self, dim_key):
        return isinstance(self._get_dim_concept(dim_key), Region)

    def _get_region_dim_key(self):
        for dim_key in self._get_dim_labels():
            if self._is_region_dim(dim_key):
                return dim_key
        return self._get_dim_labels()[0]

    def _get_y_cell_key(self):
        cell_labels = self._get_query().cell_labels
        for cell_label in cell_labels:
            if cell_label == "Count":
                return cell_label
        return cell_labels[0]

    def _get_varying_dim_keys(self, excluded_dim_keys=None):
        excluded_dim_keys = excluded_dim_keys or set()
        varying = []
        for dim_key in self._get_dim_labels():
            if dim_key in excluded_dim_keys:
                continue
            if len(self._get_unique_dim_values(dim_key)) > 1:
                varying.append(dim_key)
        return varying

    def _get_first_varying_dim_key(self, excluded_dim_keys=None):
        varying = self._get_varying_dim_keys(excluded_dim_keys)
        if varying:
            return varying[0]
        return self._get_dim_labels()[0]

    def _get_first_varying_non_region_dim_key(self):
        for dim_key in self._get_varying_dim_keys():
            if not self._is_region_dim(dim_key):
                return dim_key
        return self._get_first_varying_dim_key()

    def _init_dim_colors(self, dim_key):
        dim_values = self._get_unique_dim_values(dim_key)
        color_idx = self._get_dim_color_idx(dim_key, dim_values)
        return dim_values, color_idx

    def _get_category_dim_key(self):
        return None

    def _compute_small_categories(self):
        dim_key = self._get_category_dim_key()
        if dim_key is None:
            return set()
        cell_key = self._get_y_cell_key()
        totals = defaultdict(float)
        for datum in self.datumset:
            category = datum.dim_idx[dim_key].get_value()
            totals[category] += float(datum.cell_idx[cell_key].get_value())
        grand_total = sum(totals.values()) or 1.0
        return {
            category
            for category, total in totals.items()
            if total / grand_total < self.SMALL_CATEGORY_THRESHOLD
        }

    @cached_property
    def _small_categories(self):
        return self._compute_small_categories()

    def _remap_category(self, value):
        if value in self._small_categories:
            return self.OTHER_CATEGORY
        return value

    def _get_category_values(self, dim_key):
        values = []
        for datum in self.datumset:
            value = self._remap_category(datum.dim_idx[dim_key].get_value())
            if value not in values:
                values.append(value)
        return values

    def _init_category_colors(self, dim_key):
        dim_values = self._get_category_values(dim_key)
        color_idx = self._get_dim_color_idx(dim_key, dim_values)
        return dim_values, color_idx

    def _build_dim_title(self, y_cell_key, dim_key, relation="by"):
        return f"{y_cell_key} {relation} {dim_key}"

    def _get_query_str_for_path(self):
        source_query_str = getattr(self.datumset, "_query_str", None)
        if source_query_str and Query.OPR_LT in source_query_str:
            return source_query_str
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

    def _apply_x_order(self, x_labels, order):
        rank = {x_label: i for i, x_label in enumerate(order)}
        return sorted(x_labels, key=lambda x: rank.get(x, len(order)))

    def _get_category_cell_xy(self, datumset, dim_key, cell_key):
        totals = {}
        order = []
        for datum in datumset:
            x = self._remap_category(datum.dim_idx[dim_key].get_value())
            v = float(datum.cell_idx[cell_key].get_value())
            if x not in totals:
                totals[x] = 0.0
                order.append(x)
            totals[x] += v
        return order, [totals[x] for x in order]

    def _get_category_value_order(self, dim_key, cell_key):
        order, y_values = self._get_category_cell_xy(
            self.datumset,
            dim_key,
            cell_key,
        )
        value_by_x = dict(zip(order, y_values))
        return sorted(order, key=lambda x: value_by_x[x], reverse=True)

    def _get_ordered_category_cell_xy(
        self,
        datumset,
        dim_key,
        cell_key,
        order,
    ):
        x_labels, y_values = self._get_category_cell_xy(
            datumset,
            dim_key,
            cell_key,
        )
        value_by_x = dict(zip(x_labels, y_values))
        sorted_x = self._apply_x_order(x_labels, order)
        return sorted_x, [value_by_x[x] for x in sorted_x]

    def _collect_x_stack_totals(self, x_dim_key, cell_key, stack_dim_key):
        per_x_stack = defaultdict(lambda: defaultdict(float))
        cat_totals = defaultdict(float)
        for datum in self.datumset:
            x = datum.dim_idx[x_dim_key].get_value()
            s = datum.dim_idx[stack_dim_key].get_value()
            v = float(datum.cell_idx[cell_key].get_value())
            per_x_stack[x][s] += v
            cat_totals[s] += v
        return per_x_stack, cat_totals

    def _get_x_dominant_share_order(
        self,
        x_dim_key,
        cell_key,
        stack_dim_key,
    ):
        per_x_stack, cat_totals = self._collect_x_stack_totals(
            x_dim_key,
            cell_key,
            stack_dim_key,
        )
        dominant = max(cat_totals, key=cat_totals.get)

        def share(x):
            total = sum(per_x_stack[x].values())
            if total <= 0:
                return 0.0
            return per_x_stack[x][dominant] / total

        return sorted(per_x_stack, key=share, reverse=True)

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

    def _get_category_color(self, dim_value, color_map, default_color_idx):
        if dim_value == self.OTHER_CATEGORY:
            return self.OTHER_CATEGORY_COLOR
        if color_map:
            return color_map.get(dim_value, default_color_idx[dim_value])
        return default_color_idx[dim_value]

    def _get_dim_color_idx(self, dim_key, dim_values):
        default_color_idx = self._get_default_color_idx(dim_values)
        color_map = self._get_dim_color_map(dim_key)
        return {
            dim_value: self._get_category_color(
                dim_value,
                color_map,
                default_color_idx,
            )
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
            sub_ax.set_xticklabels(
                display_x_labels,
                fontsize=6,
                rotation=90,
                ha="center",
                va="top",
            )
            sub_ax.tick_params(axis="x", pad=1)
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
        return f"{self._get_entity_name()} {self._build_title()}"

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

    def _to_linear_rgb_channel(self, channel_value):
        if channel_value <= 0.04045:
            return channel_value / 12.92
        return ((channel_value + 0.055) / 1.055) ** 2.4

    def _get_relative_luminance(self, color):
        red, green, blue = mcolors.to_rgb(color)
        red = self._to_linear_rgb_channel(red)
        green = self._to_linear_rgb_channel(green)
        blue = self._to_linear_rgb_channel(blue)
        return 0.2126 * red + 0.7152 * green + 0.0722 * blue

    def _get_contrast_text_color(self, background_color):
        if background_color is None:
            return self.CONTRAST_DARK_TEXT_COLOR
        luminance = self._get_relative_luminance(background_color)
        if luminance > self.CONTRAST_LIGHTNESS_THRESHOLD:
            return self.CONTRAST_DARK_TEXT_COLOR
        return self.CONTRAST_LIGHT_TEXT_COLOR

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

    def _get_rect_label_rotation(self, sub_ax, rect):
        width_px, height_px = self._get_rect_size_px(sub_ax, rect)
        return 90 if height_px > width_px else 0

    def _get_best_rect_label_fontsize(self, sub_ax, rect, label, rotation):
        fig = sub_ax.figure
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        cx = rect.get_x() + rect.get_width() / 2.0
        cy = rect.get_y() + rect.get_height() / 2.0
        max_width_px, max_height_px = self._get_rect_size_px(sub_ax, rect)
        fontsize_cap = self._get_rect_fontsize_cap(sub_ax, rect)
        if fontsize_cap < self.MIN_STACK_LABEL_FONTSIZE:
            return 0
        probe = sub_ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            rotation=rotation,
        )
        best_fontsize = 0
        max_fontsize = min(self.MAX_STACK_LABEL_FONTSIZE, fontsize_cap)
        for fontsize in range(max_fontsize, 3, -1):
            probe.set_fontsize(fontsize)
            bbox = probe.get_window_extent(renderer=renderer)
            if (
                bbox.width <= max_width_px * self.STACK_LABEL_BBOX_MARGIN
                and bbox.height <= max_height_px * self.STACK_LABEL_BBOX_MARGIN
            ):
                best_fontsize = fontsize
                break
        probe.remove()
        return best_fontsize

    def _add_fitted_label_in_rect(self, sub_ax, rect, label):
        rotation = self._get_rect_label_rotation(sub_ax, rect)
        fontsize = self._get_best_rect_label_fontsize(
            sub_ax,
            rect,
            label,
            rotation,
        )
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
            rotation=rotation,
            fontsize=fontsize,
            color=self._get_contrast_text_color(rect.get_facecolor()),
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
