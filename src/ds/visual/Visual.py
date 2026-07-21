from abc import ABC, abstractmethod

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

STRIP_COLOR = "#e8e8e8"
BORDER_COLOR = "#cccccc"
TITLE_COLOR = "#333333"
SUBTITLE_COLOR = "#555555"
FONT_FAMILY = "Inter"


class Visual(ABC):

    FIGSIZE = (9, 9)
    DPI = 100

    def __init__(self, datumset, *params):
        self.datumset = datumset
        self.params = params

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
    def _image_path(self):
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
            facecolor=STRIP_COLOR,
            edgecolor=BORDER_COLOR,
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
            fontweight="bold",
            color=TITLE_COLOR,
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
            edgecolor=BORDER_COLOR,
            linewidth=2,
            zorder=5,
            clip_on=False,
        )
        fig.add_artist(border)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(BORDER_COLOR)
        ax.spines["bottom"].set_color(BORDER_COLOR)
        ax.tick_params(colors=SUBTITLE_COLOR)
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
        with plt.rc_context({"font.family": FONT_FAMILY}):
            fig, ax = plt.subplots(figsize=self.FIGSIZE, dpi=self.DPI)
            self._plot(fig, ax)
            self._apply_style(fig, ax)
            fig.savefig(self._image_path())
        plt.close(fig)
        return fig
