from abc import ABC, abstractmethod
from functools import cached_property

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from utils_future import Directory, File, Log

log = Log("Visual")


class Visual(ABC):

    FIGSIZE = (9, 9)
    DPI = 100
    STRIP_COLOR = "#e8e8e8"
    BORDER_COLOR = "#cccccc"
    TITLE_COLOR = "#333333"
    SUBTITLE_COLOR = "#555555"
    FONT_FAMILY = "Monaco"

    def __init__(self, datumset, *params):
        self.datumset = datumset
        self.params = params

    @cached_property
    def dir_visual(self) -> Directory:
        dir_visual = Directory("images", self.datumset[0].query.query_str)
        dir_visual.make()
        return dir_visual

    @cached_property
    def image_file(self) -> File:
        return File(self.dir_visual, self.__class__.__name__ + ".png")

    def _excluded_dim_keys(self):
        return set()

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

    def _build_full_title(self):
        datum = self.datumset[0]
        entity = datum.entity_class.__name__
        other = [
            f"{k} {v.get_value()}"
            for k, v in datum.dim_idx.items()
            if k not in self._excluded_dim_keys()
        ]
        suffix = " for " + " and ".join(other) if other else ""
        return f"{entity} {self._build_title()}{suffix}"

    def _add_strip(self, fig):
        strip = mpatches.Rectangle(
            (0.01, 0.90),
            0.98,
            0.08,
            transform=fig.transFigure,
            facecolor=self.STRIP_COLOR,
            edgecolor=self.BORDER_COLOR,
            linewidth=1,
            zorder=5,
            clip_on=False,
        )
        fig.add_artist(strip)
        fig.text(
            0.5,
            0.94,
            self._build_full_title(),
            ha="center",
            va="center",
            fontsize=11,
            color=self.TITLE_COLOR,
            zorder=6,
        )

    def _apply_style(self, fig, ax):
        self._add_strip(fig)
        border = mpatches.Rectangle(
            (0.01, 0.01),
            0.98,
            0.97,
            transform=fig.transFigure,
            fill=False,
            edgecolor=self.BORDER_COLOR,
            linewidth=2,
            zorder=5,
            clip_on=False,
        )
        fig.add_artist(border)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(self.BORDER_COLOR)
        ax.spines["bottom"].set_color(self.BORDER_COLOR)
        ax.tick_params(colors=self.SUBTITLE_COLOR)
        fig.text(
            0.5,
            0.02,
            self.datumset[0].query.query_str,
            ha="center",
            va="bottom",
            fontsize=7,
            color="#aaaaaa",
            zorder=6,
        )
        fig.subplots_adjust(top=0.87, bottom=0.08, left=0.1, right=0.95)

    def draw(self):
        rc = {
            "font.family": "sans-serif",
            "font.sans-serif": [self.FONT_FAMILY],
        }
        with plt.rc_context(rc):
            fig, ax = plt.subplots(figsize=self.FIGSIZE, dpi=self.DPI)
            self._plot(fig, ax)
            self._apply_style(fig, ax)
            fig.savefig(self.image_file.path)
            log.debug(f"Wrote {self.image_file}")
        plt.close(fig)
        return fig
