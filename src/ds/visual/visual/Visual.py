import glob
import os
from abc import ABC, abstractmethod

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from utils_future import Log

from ds.visual.visual.VisualCategoryMixin import VisualCategoryMixin
from ds.visual.visual.VisualColorMixin import VisualColorMixin
from ds.visual.visual.VisualContrastMixin import VisualContrastMixin
from ds.visual.visual.VisualDataMixin import VisualDataMixin
from ds.visual.visual.VisualFormatMixin import VisualFormatMixin
from ds.visual.visual.VisualLayoutMixin import VisualLayoutMixin
from ds.visual.visual.VisualParamsMixin import VisualParamsMixin
from ds.visual.visual.VisualPathMixin import VisualPathMixin
from ds.visual.visual.VisualRectFitMixin import VisualRectFitMixin
from ds.visual.visual.VisualRectLabelMixin import VisualRectLabelMixin
from ds.visual.visual.VisualTitleMixin import VisualTitleMixin
from ds.visual.visual.VisualUnderlineMixin import VisualUnderlineMixin
from ds.visual.visual.VisualXAxisMixin import VisualXAxisMixin

log = Log("Visual")

_FONTS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "..", "media", "fonts"
)
for _ttf in glob.glob(os.path.join(_FONTS_DIR, "**", "*.ttf")):
    fm.fontManager.addfont(_ttf)


class Visual(
    VisualParamsMixin,
    VisualCategoryMixin,
    VisualDataMixin,
    VisualColorMixin,
    VisualContrastMixin,
    VisualFormatMixin,
    VisualPathMixin,
    VisualTitleMixin,
    VisualXAxisMixin,
    VisualUnderlineMixin,
    VisualRectFitMixin,
    VisualRectLabelMixin,
    VisualLayoutMixin,
    ABC,
):

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
    X_TICK_FONTSIZE = 9
    X_TICK_CHAR_WIDTH_RATIO = 0.62
    X_LABEL_UNDERLINE_HALF = 0.4
    X_LABEL_UNDERLINE_LW = 3
    X_LABEL_UNDERLINE_GAP = 0.015

    def __init__(self, datumset):
        self.datumset = datumset
        self._renderer = None
        self.params = self._get_params()

    @abstractmethod
    def _plot(self, fig, ax):
        pass

    def draw(self):
        self._set_font()
        self._renderer = None
        fig, ax = plt.subplots(figsize=self.FIGSIZE, dpi=self.DPI)
        self._plot(fig, ax)
        self._add_title(fig)
        self._add_subtitle(fig)
        self._add_border(fig)
        self._apply_style(fig, fig.axes)
        fig.savefig(self.image_file.path, dpi=self.DPI, bbox_inches="tight")
        log.debug(f"Wrote {self.image_file}")
        plt.close(fig)
        return fig
