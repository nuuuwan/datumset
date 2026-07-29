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
    DPI = 100

    def __init__(self, datumset):
        self.datumset = datumset
        self._renderer = None

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
        fig.savefig(self.image_file.path, dpi=self.DPI)
        log.debug(f"Wrote {self.image_file}")
        plt.close(fig)
        return fig
